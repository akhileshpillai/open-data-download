library(ggplot2)
library(plyr)

if (!('l' %in% ls())) {
  lb <- read.csv('licensing-by-portal.csv')
  lb$prop <- 1 - (lb$no_license / lb$all)
  l <- read.csv('licensing.csv')

  l$license.reduced <- l$license_standard
  l$license.reduced[grepl('^CC', l$license_standard)] <- 'Other'
  l$license.reduced[l$license_standard == 'CC-BY-SA'] <- 'CC-BY-SA'
  # l$license.reduced[l$license_standard == 'ODbL'] <- 'Other open license'
  l$license.reduced[l$license_standard == 'GFDL'] <- 'Other open license'
  l$license.reduced[l$license_standard == 'Other open data license'] <- 'Other open license'
  l$license.reduced <- factor(l$license.reduced,
    levels = rev(c("Public domain","CC-BY-SA","ODbL","Other open license","dl-de-by-1.0","A UK Government license","Other","No license")))

  l.by.portal <- ddply(l, 'portal', function(df) {
    c(prop = sum(df$license.reduced == 'No license'))
  })
}

p1 <- ggplot(l.by.portal) + aes(x = prop) + geom_histogram() +
  scale_x_continuous('Proportion of datasets with a license') +
  scale_y_continuous('Number of portals with this proportion') +
  ggtitle('Which portals indicate the licenses of their datasets?')

p2 <- ggplot(l) + aes(x = license.reduced) + geom_bar() + coord_flip() +
  scale_x_discrete('Dataset license') +
  scale_y_continuous('Number of datasets') +
  ggtitle('Data license in use across 100 portals')

p3 <- ggplot(subset(l, portal == 'data.sfgov.org' | portal == 'data.cityofnewyork.us' | portal == 'data.cityofchicago.us' | portal == 'data.gov.uk' | portal == 'explore.data.gov' | portal == 'data.cityofsantacruz.com' | portal == 'parisdata.opendatasoft.com' | portal == 'data.oaklandnet.com')) +
  facet_wrap(~ portal) + aes(x = license.reduced) +  geom_bar() +
  # aes(fill = portal_software) +
  coord_flip() +
  scale_x_discrete('Dataset license') +
  scale_y_continuous('Number of datasets') +
  ggtitle('Licenses in use in a few portals')

plot.wrapped <- function(data) {
  ggplot(data) +
    facet_wrap(~ portal) + aes(x = license.reduced) +  geom_bar() +
    aes(fill = portal_software) +
    coord_flip() +
    scale_x_discrete('Dataset license') +
    scale_y_continuous('Number of datasets') +
    ggtitle('Dataset license by portal')
}

p4 <- plot.wrapped(l)
p5 <- plot.wrapped(subset(l, portal != 'publicdata.eu'))

p <- function(.p, fn) {
  png(fn, width = 840, height = 840, res = 150)
  print(.p)
  dev.off()
}

main <- function() {
  p(p1, 'p1.png')
  p(p2, 'p2.png')
  p(p3, 'p3.png')
}

png('p4.png',  width = 2 * 840, height = 2 * 840, res = 100)
print(p4)
dev.off()

png('p5.png',  width = 2 * 840, height = 2 * 840, res = 100)
print(p5)
dev.off()
