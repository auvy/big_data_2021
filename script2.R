#install.packages("dplyr")
#install.packages("ggplot2")
#library(dplyr)
#library(ggplot2)
#p <- ggplot(flats, aes(x=Загальна_площа)) + geom_bar(fill="lightblue", col="grey") + ylab('Кількість')
#p
ggplot(flats, aes(x=Загальна_площа, y=Ціна)) + geom_point()