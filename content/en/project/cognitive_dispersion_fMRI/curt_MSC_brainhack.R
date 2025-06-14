

# May 29, 2025 
# calculate MSC dispersion 

# data ----
getwd()
setwd("C:/Users/Admin/Downloads/@Sinica-NTU/Lab_NTU/Cognitive dispersion/Ref/MSC")

library(readxl)
MSC_test <- read_excel("MSC_test.xlsx", sheet = "Sheet3")

hist.data.frame(MSC_test[, 2:8])
psych::describe(MSC_test, fast = T)

# calculate dispersion ----

#### OTBM, ISD 

MSC_test$OTBM <- rowMeans(
  MSC_test[, c(2:8)])

MSC_test <- MSC_test %>%
  rowwise() %>%
  mutate(ISD = stats::sd(c_across(EF_DCCS:Language_Vocab)),
         CoV = ISD/OTBM)

hist.data.frame(MSC_test[, 9:11])
dev.off()

#GGally::ggpairs(dispersion_TOT_APR25_Tscore, columns = c(4:5, 28:30, 3), 
#                aes(color = label_HC_MCI)) + 
#  theme_bw()

MSC_test %>% select(ID, OTBM, ISD) %>% arrange(ISD)
# highest ISD: S04 > S03 > S10 
MSC_test %>% select(ID, OTBM, ISD) %>% arrange(OTBM)
# highest OTBM: S09 > S10 > S02 

plot(MSC_test$OTBM, MSC_test$ISD)

library(ggrepel)
ggplot(MSC_test, aes(OTBM, ISD)) +
  geom_point(color = "blue") +
  geom_text_repel(aes(label = ID), color = "blue") +
  theme(
    axis.text = element_text(color = "black", size = 12),
    axis.title = element_text(size = 13, face = "bold"))

ggplot(MSC_test, aes(OTBM, ISD)) +
  theme(
    axis.text = element_text(color = "black", size = 12),
    axis.title = element_text(size = 13, face = "bold"))

library(rstatix)
MSC_test %>% cor_test(OTBM, ISD) # p = .40, r = -0.32

# CHOOSE: S02 (high OTBM, low ISD)  34yo male, edu=28
#         S04 (high ISD, low OTBM)  28yo female, edu=22


# neuropsy fig ----

library(reshape2)
MSC_test_melt <- melt(MSC_test[, 1:8])
head(MSC_test_melt)

ggplot(MSC_test_melt, 
       aes(x=variable,
           y=value, group=ID)) +
  geom_line(aes(color=ID), linewidth = 0.9) +
  geom_point(aes(color=ID), size = 2) +
  theme_classic() +
  scale_color_manual(values=c("grey90", "grey90", "red", "firebrick", 
                              "grey90", "grey90", "grey90", "grey90", "grey90")) +
  theme(axis.text.x = element_text(color = "black", size = 9, angle = 45, hjust = 1),
        axis.text.y = element_text(color = "black", size = 11),
        axis.title = element_text(size = 14, face = "bold"),
        legend.position="right", legend.text = element_text(size = 13)) +
  labs(x = "Cognitive Test", y = "Standard score", face = "bold") 

ggplot(MSC_test_melt, 
       aes(x=variable,
           y=value, group=ID)) +
  geom_line(aes(color=ID), linewidth = 0.9) +
  geom_point(aes(color=ID), size = 2) +
  theme_classic() +
  theme(axis.text.x = element_text(color = "black", size = 11, angle = 45, hjust = 1),
        axis.text.y = element_text(color = "black", size = 11),
        axis.title = element_text(size = 14, face = "bold"),
        legend.position="top", legend.text = element_text(size = 13)) +
  labs(x = "Cognitive Test", y = "Standard score", face = "bold") 




