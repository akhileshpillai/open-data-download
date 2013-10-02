library(ggplot2)

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
  l$license.reduced <- factor(l$license.reduced)
}

p1 <- ggplot(lb) + aes(x = prop) + geom_histogram() +
  scale_x_continuous('Proportion of datasets with a the license field filled in') +
  scale_y_continuous('Number of portals with this proportion') +
  ggtitle('Which portals indicate the licenses of their datasets?')

p2 <- ggplot(l) + aes(x = license_standard) + geom_bar() + coord_flip() +
  scale_x_discrete('Dataset license') +
  scale_y_continuous('Number of datasets') +
  ggtitle('Data license in use across 100 portals')

p3 <- ggplot(subset(l, portal == 'data.sfgov.org' | portal == 'data.cityofnewyork.us' | portal == 'data.cityofchicago.us' | portal == 'data.gov.uk' | portal == 'explore.data.gov' | portal == 'data.cityofsantacruz.com' | portal == 'parisdata.opendatasoft.com' | portal == 'data.oaklandnet.com')) +
  facet_wrap(~ portal) + aes(x = license_standard) +  geom_bar() +
  # aes(fill = portal_software) +
  coord_flip() +
  scale_x_discrete('Dataset license') +
  scale_y_continuous('Number of datasets') +
  ggtitle('Licenses in use in a few portals')

p <- function(.p, fn) {
  png(fn, width = 840, height = 840, res = 150)
  print(.p)
  dev.off()
}

p(p1, 'p1.png')
p(p2, 'p2.png')
p(p3, 'p3.png')
