import pandas as pd
import biogeme.database as db
import biogeme.biogeme as bio
import biogeme.version as ver
import biogeme.models as models
from biogeme.expressions import Beta, bioNormalCdf, Elem, log
import math
import numpy as np

# Read the data
df = pd.read_csv("./Data/DATABASE1.csv")
database = db.Database("PROJECT", df)

# The following statement allows you to use the names of the variable
# as Python variable.

globals().update(database.variables)

# Parameters to be estimated
ASC_CAR_DRIVER = Beta("ASC_CAR_DRIVER", 0, None, None, 0)
ASC_CAR_PASSENGER = Beta("ASC_CAR_PASSENGER", 0, None, None, 0)
ASC_METRO = Beta("ASC_METRO", 0, None, None, 0)
ASC_BRT = Beta("ASC_BRT", 0, None, None, 0)
ASC_BUS = Beta("ASC_BUS", 0, None, None, 0)
ASC_TAXI = Beta("ASC_TAXI", 0, None, None, 0)
ASC_SNAPP = Beta("ASC_SNAPP", 0, None, None, 0)
ASC_PHONETAXI = Beta("ASC_PHONETAXI", 0, None, None, 0)
ASC_MOTORCYCLE = Beta("ASC_MOTORCYCLE", 0, None, None, 0)
ASC_BIKE = Beta("ASC_BIKE", 0, None, None, 0)
ASC_SERVICE = Beta("ASC_SERVICE", 0, None, None, 0)
ASC_WALK = Beta("ASC_WALK", 0, None, None, 0)
ASC_SCOOTER_PT = Beta("ASC_SCOOTER_PT", 0, None, None, 0)

B_TIME = Beta("B_TIME", 0, None, None, 0)  # FOR CAR, MOTORCYLCE, BIKE, SERVICE, WALK
B_COST = Beta("B_COST", 0, None, None, 0)  # FOR ALL
B_SAFETY = Beta("B_SAFETY", 0, None, None, 0)  # FOR ALL
B_COMFORT = Beta("B_COMFORT", 0, None, None, 0)  # FOR ALL

B_PT_ACC_TIME = Beta("B_PT_ACC_TIME", 0, None, None, 0)  # FOR PT
B_PT_IVT_TIME = Beta("B_PT_IVT_TIME", 0, None, None, 0)  # FOR PT
B_PT_WAIT_TIME = Beta("B_PT_WAIT_TIME", 0, None, None, 0)  # FOR PT
B_PT_ACC_COST = Beta("B_PT_ACC_COST", 0, None, None, 0)  # FOR PT
B_PT_ACC_TOD_TIME = Beta("B_PT_ACC_TOD_TIME", 0, None, None, 0)  # FOR PT
B_PT_ACC_TOD_COST = Beta("B_PT_ACC_TOD_COST", 0, None, None, 0)  # FOR PT

B_O_ACC_DIST = Beta("B_O_ACC_DIST", 0, None, None, 0)
B_D_ACC_DIST = Beta("B_D_ACC_DIST", 0, None, None, 0)
B_D_PARK = Beta("B_D_PARK", 0, None, None, 0)
B_O_ACC_MODE = Beta("B_O_ACC_MODE", 0, None, None, 0)
B_D_ACC_MODE = Beta("B_D_ACC_MODE", 0, None, None, 0)

# Lam1 = Beta("LAMBDA_T", 1, 0, None, 1)
# Lam2 = Beta("LAMBDA_C", 1, 0, None, 1)
####################### Dummy #########################
BGENDER1 = Beta("BGENDER1", 0, -1000, 1000, 0)
IFGENDER1 = database.DefineVariable("IFGENDER1", GENDER == 1)

BAGE1 = Beta("BAGE1", 0, -1000, 1000, 0)
IFAGE1 = database.DefineVariable("IFAGE1", AGE == 1)
BAGE2 = Beta("BAGE2", 0, -1000, 1000, 0)
IFAGE2 = database.DefineVariable("IFAGE2", AGE == 2)
BAGE3 = Beta("BAGE3", 0, -1000, 1000, 0)
IFAGE3 = database.DefineVariable("IFAGE3", AGE == 3)
BAGE4 = Beta("BAGE4", 0, -1000, 1000, 0)
IFAGE4 = database.DefineVariable("IFAGE4", AGE == 4)
BAGE5 = Beta("BAGE5", 0, -1000, 1000, 0)
IFAGE5 = database.DefineVariable("IFAGE5", AGE == 5)
BAGE6 = Beta("BAGE6", 0, -1000, 1000, 0)
IFAGE6 = database.DefineVariable("IFAGE6", AGE == 6)

BOCCU1 = Beta("BOCCU1", 0, -1000, 1000, 0)
IFOCCU1 = database.DefineVariable("IFOCCU1", OCCU == 1)
BOCCU2 = Beta("BOCCU2", 0, -1000, 1000, 0)
IFOCCU2 = database.DefineVariable("IFOCCU2", OCCU == 2)
BOCCU3 = Beta("BOCCU3", 0, -1000, 1000, 0)
IFOCCU3 = database.DefineVariable("IFOCCU3", OCCU == 3)
BOCCU4 = Beta("BOCCU4", 0, -1000, 1000, 0)
IFOCCU4 = database.DefineVariable("IFOCCU4", OCCU == 4)
BOCCU5 = Beta("BOCCU5", 0, -1000, 1000, 0)
IFOCCU5 = database.DefineVariable("IFOCCU5", OCCU == 5)
BOCCU6 = Beta("BOCCU6", 0, -1000, 1000, 0)
IFOCCU6 = database.DefineVariable("IFOCCU6", OCCU == 6)
BOCCU7 = Beta("BOCCU7", 0, -1000, 1000, 0)
IFOCCU7 = database.DefineVariable("IFOCCU7", OCCU == 7)
BOCCU8 = Beta("BOCCU8", 0, -1000, 1000, 0)
IFOCCU8 = database.DefineVariable("IFOCCU8", OCCU == 8)


BEDU1 = Beta("BEDU1", 0, -1000, 1000, 0)
IFEDU1 = database.DefineVariable("IFEDU1", EDU == 1)
BEDU2 = Beta("BEDU2", 0, -1000, 1000, 0)
IFEDU2 = database.DefineVariable("IFEDU2", EDU == 2)
BEDU3 = Beta("BEDU3", 0, -1000, 1000, 0)
IFEDU3 = database.DefineVariable("IFEDU3", EDU == 3)
BEDU4 = Beta("BEDU4", 0, -1000, 1000, 0)
IFEDU4 = database.DefineVariable("IFEDU4", EDU == 4)

BINC1 = Beta("BINC1", 0, -1000, 1000, 0)
IFINC1 = database.DefineVariable("IFINC1", HINCOME == 1)
BINC2 = Beta("BINC2", 0, -1000, 1000, 0)
IFINC2 = database.DefineVariable("IFINC2", HINCOME == 2)
BINC3 = Beta("BINC3", 0, -1000, 1000, 0)
IFINC3 = database.DefineVariable("IFINC3", HINCOME == 3)
BINC4 = Beta("BINC4", 0, -1000, 1000, 0)
IFINC4 = database.DefineVariable("IFINC4", HINCOME == 4)

BBIKEFR1 = Beta("BBIKEFR1", 0, -1000, 1000, 0)
IFBIKEFR1 = database.DefineVariable("IFBIKEFR1", BIKE_FR == 1)
BBIKEFR2 = Beta("BBIKEFR2", 0, -1000, 1000, 0)
IFBIKEFR2 = database.DefineVariable("IFBIKEFR2", BIKE_FR == 2)
BBIKEFR3 = Beta("BBIKEFR3", 0, -1000, 1000, 0)
IFBIKEFR3 = database.DefineVariable("IFBIKEFR3", BIKE_FR == 3)
BBIKEFR4 = Beta("BBIKEFR4", 0, -1000, 1000, 0)
IFBIKEFR4 = database.DefineVariable("IFBIKEFR4", BIKE_FR == 4)

BBIKEPOR1 = Beta("BBIKEPOR1", 0, -1000, 1000, 0)
IFBIKEPOR1 = database.DefineVariable("IFBIKEPOR1", BIKE_POR == 1)
BBIKEPOR2 = Beta("BBIKEPOR2", 0, -1000, 1000, 0)
IFBIKEPOR2 = database.DefineVariable("IFBIKEPOR2", BIKE_POR == 2)
BBIKEPOR3 = Beta("BBIKEPOR3", 0, -1000, 1000, 0)
IFBIKEPOR3 = database.DefineVariable("IFBIKEPOR3", BIKE_POR == 3)
BBIKEPOR4 = Beta("BBIKEPOR4", 0, -1000, 1000, 0)
IFBIKEPOR4 = database.DefineVariable("IFBIKEPOR4", BIKE_POR == 4)
BBIKEPOR5 = Beta("BBIKEPOR5", 0, -1000, 1000, 0)
IFBIKEPOR5 = database.DefineVariable("IFBIKEPOR5", BIKE_POR == 5)
BBIKEPOR6 = Beta("BBIKEPOR6", 0, -1000, 1000, 0)
IFBIKEPOR6 = database.DefineVariable("IFBIKEPOR6", BIKE_POR == 6)
BBIKEPOR7 = Beta("BBIKEPOR7", 0, -1000, 1000, 0)
IFBIKEPOR7 = database.DefineVariable("IFBIKEPOR7", BIKE_POR == 7)
BBIKEPOR8 = Beta("BBIKEPOR8", 0, -1000, 1000, 0)
IFBIKEPOR8 = database.DefineVariable("IFBIKEPOR8", BIKE_POR == 8)
BBIKEPOR9 = Beta("BBIKEPOR9", 0, -1000, 1000, 0)
IFBIKEPOR9 = database.DefineVariable("IFBIKEPOR9", BIKE_POR == 9)
#######################################################

# Definition of the utility functions
# V_Auto    = ASC_AUTO + B_T * models.boxcox(tA, Lam1) + B_C * models.boxcox(cA, Lam2)
# V_Transit = ASC_TRANSIT + B_T * models.boxcox(tT, Lam1) + B_C * models.boxcox(cT, Lam2)

# Definition of the utility functions
V_CarDriver = (
    ASC_CAR_DRIVER
    + B_TIME * CAR_TIME
    + B_COST * CAR_COST
    + BGENDER1 * IFGENDER1
    + BAGE1 * IFAGE1
    + BAGE2 * IFAGE2
    + BAGE3 * IFAGE3
    + BAGE4 * IFAGE4
    + BAGE5 * IFAGE5
    + BAGE6 * IFAGE6
    + BEDU1 * IFEDU1
    + BEDU2 * IFEDU2
    + BEDU3 * IFEDU3
    + BEDU4 * IFEDU4
    + BOCCU1 * IFOCCU1
    + BOCCU2 * IFOCCU2
    + BOCCU3 * IFOCCU3
    + BOCCU4 * IFOCCU4
    + BOCCU5 * IFOCCU5
    + BOCCU6 * IFOCCU6
    + BINC1 * IFINC1
    + BINC2 * IFINC2
    + BINC3 * IFINC3
    + BINC4 * IFINC4
    # + B_SAFETY * CAR_SAFETY
    # + B_COMFORT * CAR_COMFORT
)
V_CarPassenger = (
    ASC_CAR_PASSENGER
    + B_TIME * CAR_PASS_TIME
    + B_COST * CAR_PASS_COST
    # + B_SAFETY * CAR_PASS_SAFETY
    # + B_COMFORT * CAR_PASS_COMFORT
)
V_Metro = (
    ASC_METRO
    + B_PT_ACC_TIME * METRO_ACC_TIME
    + B_PT_IVT_TIME * METRO_IVT_TIME
    + B_PT_WAIT_TIME * METRO_WAIT_TIME
    + B_PT_ACC_COST * METRO_ACC_COST
    + B_COST * METRO_COST
    # + B_SAFETY * METRO_SAFTY
    # + B_COMFORT * METRO_COMFORT
)
V_Brt = (
    ASC_BRT
    + B_PT_ACC_TIME * BRT_ACC_TIME
    + B_PT_IVT_TIME * BRT_IVT_TIME
    + B_PT_WAIT_TIME * BRT_WAIT_TIME
    + B_PT_ACC_COST * BRT_ACC_COST
    + B_COST * BRT_COST
    # + B_SAFETY * BRT_SAFTY
    # + B_COMFORT * BRT_COMFORT
)
V_Bus = (
    ASC_BUS
    + B_PT_ACC_TIME * BUS_ACC_TIME
    + B_PT_IVT_TIME * BUS_IVT_TIME
    + B_PT_WAIT_TIME * BUS_WAIT_TIME
    + B_PT_ACC_COST * BUS_ACC_COST
    + B_COST * BUS_COST
    # + B_SAFETY * BUS_SAFTY
    # + B_COMFORT * BUS_COMFORT
)
V_Taxi = (
    ASC_TAXI
    + B_PT_ACC_TIME * TAXI_ACC_TIME
    + B_PT_IVT_TIME * TAXI_IVT_TIME
    + B_PT_WAIT_TIME * TAXI_WAIT_TIME
    + B_PT_ACC_COST * TAXI_ACC_COST
    + B_COST * TAXI_COST
    # + B_SAFETY * TAXI_SAFTY
    # + B_COMFORT * TAXI_COMFORT
)
V_Snapp = (
    ASC_SNAPP
    + B_PT_IVT_TIME * SNAPP_IVT
    + B_PT_WAIT_TIME * SNAPP_WAIT_TIME
    + B_COST * SNAPP_COST
    # + B_SAFETY * SNAPP_SAFETY
    # + B_COMFORT * SNAPP_COMFORT
)
V_Phonetaxi = (
    ASC_PHONETAXI
    + B_PT_IVT_TIME * PHONETAXI_IVT
    + B_PT_WAIT_TIME * PHONETAXI_WAIT_TIME
    + B_COST * PHONETAXI_COST
    # + B_SAFETY * PHONETAXI_SAFETY
    # + B_COMFORT * PHONETAXI_COMFORT
)
V_Motorcycle = (
    ASC_MOTORCYCLE
    + B_TIME * MOTORCYCLE_TIME
    + B_COST * MOTORCYCLE_COST
    # + B_SAFETY * MOTORCYCLE_SAFETY
    # + B_COMFORT * MOTORCYCLE_COMFORT
)
V_Bike = (
    ASC_BIKE
    + B_TIME * BIKE_TIME
    + B_COST * BIKE_COST
    # + BBIKEFR1 * IFBIKEFR1
    # + BBIKEFR2 * IFBIKEFR2
    # + BBIKEFR3 * IFBIKEFR3
    # + BBIKEFR4 * IFBIKEFR4
    # + BBIKEPOR1 * IFBIKEPOR1
    # + B_SAFETY * BIKE_SAFETY
    # + B_COMFORT * BIKE_COMFORT
)
V_Walk = ASC_WALK + B_TIME * WALK_TIME
V_Service = (
    ASC_SERVICE
    + B_TIME * SERVICE_TIME
    + B_COST * SERVICE_COST
    # + B_SAFETY * SERVICE_SAFETY
    # + B_COMFORT * SERVICE_COMFORT
)
B_SC_ACC_TIME = Beta("B_SC_ACC_TIME", 0, None, None, 0)
B_SC_ACC_COST = Beta("B_SC_ACC_COST", 0, None, None, 0)
B_SC_ACC_DIST = Beta("B_SC_ACC_DIST", 0, None, None, 0)
# فرض 5 دقیقه زمان دسترسی چون برای همه دیتا ها زمان دسترسی رو نداریم
# همچنین فرض مترو به عنوان مد حمل و نقل عمومی
V_Scooter_Pt = (
    # ASC_SCOOTER_PT
    # + B_PT_ACC_TIME * 5
    # + B_PT_IVT_TIME * METRO_IVT_TIME
    # + B_SCOOTER_COST * 10000
    # + B_O_ACC_DIST * 250
    ASC_SCOOTER_PT
    + B_SC_ACC_TIME * 5
    + B_PT_IVT_TIME * METRO_IVT_TIME
    + B_PT_WAIT_TIME * METRO_WAIT_TIME
    + B_SC_ACC_COST * 10000
    + B_SC_ACC_DIST * 250
    + B_COST * METRO_COST
    # + B_SAFETY * METRO_SAFTY
    # + B_COMFORT * METRO_COMFORT
)
# Associate utility functions with the numbering of alternatives
V = {
    1: V_CarDriver,
    2: V_CarPassenger,
    3: V_Metro,
    4: V_Brt,
    5: V_Bus,
    6: V_Taxi,
    7: V_Snapp,
    8: V_Phonetaxi,
    9: V_Motorcycle,
    10: V_Bike,
    11: V_Walk,
    12: V_Service,
    99: V_Scooter_Pt,
}
METRO_AV = database.DefineVariable("METRO_AV", O_METRO_ACC * D_METRO_ACC == 1)
BRT_AV = database.DefineVariable("BRT_AV", O_BRT_ACC * D_BRT_ACC == 1)
BUS_AV = database.DefineVariable("BUS_AV", O_BUS_ACC * D_BUS_ACC == 1)
TAXI_AV = database.DefineVariable("TAXI_AV", O_TAXI_ACC * D_TAXI_ACC == 1)
# Associate the availability conditions with the alternatives
av = {
    1: O_CAR_DRIVER_ACC,
    2: O_CAR_PASSE_ACC,
    3: METRO_AV,
    4: BRT_AV,
    5: BUS_AV,
    6: TAXI_AV,
    7: SNAPP_ACC,
    8: PHONE_TAXI_ACC,
    9: MOTORCYCLE_ACC,
    10: BIKE_ACC,
    11: 1,
    12: SERVICE_ACC,
    99: 1,
}

# for Logit use the following ...
logprob = models.loglogit(V, av, FINAL_CHOICE)

# Create the Biogeme object
biogeme = bio.BIOGEME(database, logprob)
biogeme.modelName = "Generic1"

# Estimate the parameters
results = biogeme.estimate()
print(results)

# Get the results in a pandas table
pandasResults = results.getEstimatedParameters(onlyRobust=False)
print(pandasResults)
