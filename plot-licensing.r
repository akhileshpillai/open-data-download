library(ggplot2)

l <- read.csv('licensing-by-portal.csv')
l$prop <- l$no_license / l$all


p1 <- ggplot(l) + aes(x = prop) + geom_histogram() +
  scale_x_continuous('Proportion of datasets with a the license field filled in') +
  scale_y_continuous('Number of portals with this proportion') +
  ggtitle('Which portals indicate the licenses of their datasets?')
