library(ggplot2)

portals <- read.csv('ckan_workingness.csv')
p1 <- ggplot(portals) + aes(x = connects) + geom_bar()
p2 <- ggplot(subset(portals, connects)) + aes(x = datasets) +
  geom_histogram() +
  scale_x_log10('Number of datasets on the portal', breaks = 10^(0:5)) +
  scale_y_continuous('Number of portals with this many datasets.')

p3 <- ggplot(subset(portals, connects)) +
  aes(x = datasets) + geom_histogram() +
  scale_x_continuous('Number of datasets on the portal') +
  scale_y_continuous('Number of portals with this many datasets.')

p4 <- ggplot(subset(portals, connects & datasets < 10000)) +
  aes(x = datasets) + geom_histogram() +
  scale_x_continuous('Number of datasets on the portal') +
  scale_y_continuous('Number of portals with this many datasets.')


# print(p1)
# print(p2)
print(p4)
