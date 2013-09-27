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
# print(p4)

print(subset(portals, datasets > 1000))

print('These are mostly not CKAN portals, even though they were supposed to be.')
print(subset(portals, !connects))

# print('These are failing because they\'re not the root domain.')
# print(subset(portals, grepl('/', portal)))
#                           portal connects datasets
# 3  www.amsterdamopendata.nl/home    FALSE       NA
# 23              data.gov.uk/data    FALSE       NA


# And then, what's wrong with the non-connecting portals?
