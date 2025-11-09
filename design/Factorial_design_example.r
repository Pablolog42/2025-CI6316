install.packages('choiceDes')
library(choiceDes)
###Define attributes and levels
attributes = data.frame(RH_cost=c(15,20,25),
                        RH_travel_time = c(20, 30,40),
                        RH_Comfort= c(7,8,9),
                    
                        metro_cost=c(1,2,3),
                        metro_travel_time = c(50, 60,70),
                        metro_Comfort= c(4,5,6),
           
                        Bus_cost=c(1,2,3),
                        Bus_travel_time = c(60, 70,80),
                        Bus_Comfort= c(3,4,5))

nb=4 ## 4 blocks, one per device
sets=12 ##number of choice tasks per block
alts=1 ## number of alternatives. For labeled experiments, use 1 alternative but with alternatives-specific factors

cands=gen.factorial(rep(3,8), factors="all") ## 3 alts x 3 atrributes x 3 levels per attribute, but the cost of bus is the same as the metro

set.seed(1211)

design=dcm.design.cand(cands, nb, sets, alts, fname=NULL, Rd=20, print=TRUE)

levels=design$levels
rownames(levels)=NULL


N=50## number of participants
random_blocks=c()
design_matrix=c()
while(length(random_blocks)<(N*nb)){
  blocks_ind=sample(1:nb,nb,replace=FALSE)
  random_blocks=c(random_blocks,blocks_ind)
  idx=order(match(levels$vers,blocks_ind))
  levels_reorder=levels[idx,]
  design_matrix=rbind(design_matrix,
                      data.frame(Block=levels_reorder$vers,
                                 Device=rep(c('Monitor','Laptop','Tablet','Smartphone'),each=12),
                                 RH_cost=attributes$RH_cost[levels_reorder$x1],
                                 RH_travel_time=attributes$RH_travel_time[levels_reorder$x2],
                                 RH_Comfort=attributes$RH_Comfort[levels_reorder$x3],
                                 metro_cost=attributes$metro_cost[levels_reorder$x4],
                                 metro_travel_time=attributes$metro_travel_time[levels_reorder$x5],
                                 metro_Comfort=attributes$metro_Comfort[levels_reorder$x6],
                                 Bus_cost= attributes$metro_cost[levels_reorder$x4], ## repeat metro cost
                                 Bus_travel_time=attributes$Bus_travel_time[levels_reorder$x7],
                                 Bus_Comfort=attributes$Bus_Comfort[levels_reorder$x8]))
}


head(design_matrix)
dim(design_matrix)
#48*50


## now save them in separate files, just because it's easy to upload to pavlovia
write.csv(design_matrix[design_matrix$Device=='Monitor',],'Design_3x3_transport1_monitor.csv',row.names = FALSE)
write.csv(design_matrix[design_matrix$Device=='Laptop',],'Design_3x3_transport2_laptop.csv',row.names = FALSE)
write.csv(design_matrix[design_matrix$Device=='Tablet',],'Design_3x3_transport3_tablet.csv',row.names = FALSE)
write.csv(design_matrix[design_matrix$Device=='Smartphone',],'Design_3x3_transport4_smartphone.csv',row.names = FALSE)

## also save the complete file
write.csv(design_matrix,'Design_3x3_transport.csv',row.names = FALSE)
