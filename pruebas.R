library(BoolNet)
setwd('/Users/mariana/Library/Mobile Documents/com~apple~CloudDocs/redes_alfredo/red_de_decision')

net_WT <- loadNetwork('original_pablo.txt')
# net_WT_daño <- fixGenes(net, 1, 1) # red WT con daño que no se logra reparar
# net_AF <- fixGenes(net, 4, 0) # red con A. de Fanconi
# net_AF_daño <- fixGenes(net_AF, 1, 1) # red con A. de Fanconi y daño siempre activo
# net_AF_TNFa <- fixGenes(net_AF, 11, 1) # red con AF y mutante en TNFa
# net_AF_TNFa_daño <- fixGenes(net_AF_TNFa, 1, 1) # red con AF y mutante en TNFa, daño siempre activo
# net_AF_Mdm2 <- fixGenes(net_AF,9,1) # red con AF y mutante Mdm2
# net_AF_Mdm2_daño <- fixGenes(net_AF_Mdm2,1,1) # red con AF y mutante Mdm2, daño siempre activo
# net_AF_TNFa_TGFb <- fixGenes(net_AF_TNFa,13,1) # red con AF y doble mutante TNFa y TGFb
# net_AF_TNFa_TGFb_daño <- fixGenes(net_AF_TNFa_TGFb,1,1) # red con AF y doble mutante TNFa y TGFb, daño siempre activo
# net_AF_TNFa_Wip1 <- fixGenes(net_AF_TNFa, 8, 0) # red AF y doble mutante TNFa y Wip1
# net_AF_TNFa_Wip1_daño <- fixGenes(net_AF_TNFa_Wip1, 1, 1) # red AF y doble mutante TNFa y Wip1, daño siempre activo
# net_WT_TNFa <- fixGenes(net_WT,11,1) #red WT con TNFa
# net_WT_TNFa_daño <- fixGenes(net_WT_daño,11,1) #red WT con TNFa y daño siempre activos
# net_WT_Mdm2 <- fixGenes(net_WT,9,1)
# net_WT_Mdm2_daño <- fixGenes(net_WT_Mdm2,1,1)
# net_WT_TNFa_TGFb <- fixGenes(net_WT_TNFa, 13, 1)
# net_WT_TNFa_TGFb_daño <- fixGenes(net_WT_TNFa_TGFb, 1, 1)
# net_WT_TNFa_Wip1 <- fixGenes(net_WT_TNFa, 8,0)
# net_WT_TNFa_Wip1_daño <- fixGenes(net_WT_TNFa_Wip1, 1,1)


attr <- getAttractors(net_WT)
plotAttractors(attr)

#edo_ini <- c(1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0)
#edo_ini <- c(1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0)
#plotSequence(net_WT_TNFa_Wip1_daño, edo_ini)


