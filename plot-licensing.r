library(ggplot2)

if (!('l' %in% ls())) {
  lb <- read.csv('licensing-by-portal.csv')
  lb$prop <- 1 - (lb$no_license / lb$all)
  l <- read.csv('licensing.csv')
}

p1 <- ggplot(lb) + aes(x = prop) + geom_histogram() +
  scale_x_continuous('Proportion of datasets with a the license field filled in') +
  scale_y_continuous('Number of portals with this proportion') +
  ggtitle('Which portals indicate the licenses of their datasets?')

p2 <- ggplot(l) + aes(x = license_standard) + geom_bar()

p3 <- ggplot(subset(l, portal == 'data.sfgov.org' | portal == 'data.cityofnewyork.us' | portal == 'data.cityofchicago.us' | portal == 'data.gov.uk' | portal == 'explore.data.gov' | portal == 'data.cityofsantacruz.com' | portal == 'parisdata.opendatasoft.com' | portal == 'data.oaklandnet.com')) +
  facet_wrap(~ portal) + aes(x = license_standard, fill = portal_software) + geom_bar() +
  coord_flip()

p <- function(.p, fn) {
  png(fn, width = 840, height = 840)
  print(.p)
  dev.off()
}

p(p1, 'p1.png')
p(p2, 'p2.png')
p(p3, 'p3.png')
