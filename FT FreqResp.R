rm(list=ls())

library(dplyr)
library(plotly)

pth  <- "/Users/test/Desktop/FR/"
setwd(pth)
getwd()


 
filez <- list.files(path=pth, pattern=".csv$", full.names=FALSE)

for(i in filez) {
    dater<- read.csv((i), header = TRUE,
                 sep = ",",
                 dec = ".",
                 fill = TRUE,
                 comment.char = "",
                 stringsAsFactors = FALSE)
    assign(i, dater)
}

# Extracts target specific data
fish1_depth <- dater[6,1:3]   # selects depth of first 3 pings
fish1_id <- filez[1]
freq<-dater$Target_index[7:length(dater$Target_index)]   #selects bandwidth 

# Extracts observations from Fish 1
fish1_p1<-as.numeric(dater$X0[7:length(dater$X0)])  #Selects fish in Ping 3927, but not very smartly...
fish1_p2 <- as.numeric(dater$X0[7:length(dater$X1)])
fish1_p3 <- as.numeric(dater$X0[7:length(dater$X2)])

#computes average TS
lin_ts_fish1_p1 <- 10^(fish1_p1/10)
lin_ts_fish1_p2 <- 10^(fish1_p2/10)
lin_ts_fish1_p3 <- 10^(fish1_p3/10)

avg_ts <- 10*log10(mean(lin_ts_fish1_p1,lin_ts_fish1_p2,lin_ts_fish1_p3))

# combine dataframes for fish 1
comboz<- data.frame(freq,fish1_p1,fish1_p2,fish1_p3, avg_ts)

# Plots freq reaponse of Fish1
p <- plot_ly(comboz, x = ~freq, y = ~fish1_p1, name = 'Ping1', type = 'scatter', mode = 'lines') %>%
  add_trace(y = ~fish1_p2, name = 'Ping2', mode = 'lines+markers') %>%
  add_trace(y = ~fish1_p3, name = 'Ping3', mode = 'markers')
  add_trace(y = ~avg_ts, name = 'Mean TS', mode = 'markers')

