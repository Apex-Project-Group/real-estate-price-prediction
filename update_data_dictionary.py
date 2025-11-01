import pandas as pd

# Load the current data dictionary
df_dict = pd.read_excel("docs/data_dictionary.xlsx")

print(f"Loaded data dictionary with {len(df_dict)} features")

# Create comprehensive descriptions for all features
feature_descriptions = {
    "Order": "Observation number (sequential identifier for each property record)",
    "PID": "Parcel Identification Number (unique property identifier)",
    "MS SubClass": "Identifies the type of dwelling involved in the sale (e.g., 20=1-Story 1946+, 60=2-Story 1946+)",
    "MS Zoning": "General zoning classification of the sale (e.g., RL=Residential Low Density, RM=Residential Medium Density)",
    "Lot Frontage": "Linear feet of street connected to property",
    "Lot Area": "Lot size in square feet",
    "Street": "Type of road access to property (Grvl=Gravel, Pave=Paved)",
    "Alley": "Type of alley access to property (Grvl=Gravel, Pave=Paved, NA=No alley access)",
    "Lot Shape": "General shape of property (Reg=Regular, IR1=Slightly irregular, IR2=Moderately irregular, IR3=Irregular)",
    "Land Contour": "Flatness of the property (Lvl=Near Flat/Level, Bnk=Banked, HLS=Hillside, Low=Depression)",
    "Utilities": "Type of utilities available (AllPub=All public utilities, NoSewr=No sewer, NoSeWa=No sewer or water)",
    "Lot Config": "Lot configuration (Inside=Inside lot, Corner=Corner lot, CulDSac=Cul-de-sac, FR2=Frontage on 2 sides)",
    "Land Slope": "Slope of property (Gtl=Gentle slope, Mod=Moderate slope, Sev=Severe slope)",
    "Neighborhood": "Physical locations within Ames city limits (e.g., CollgCr=College Creek, OldTown=Old Town)",
    "Condition 1": "Proximity to various conditions (Artery=Adjacent to arterial street, Feedr=Adjacent to feeder street, Norm=Normal)",
    "Condition 2": "Proximity to various conditions (if more than one is present)",
    "Bldg Type": "Type of dwelling (1Fam=Single-family Detached, 2FmCon=Two-family Conversion, Duplx=Duplex, TwnhsE=Townhouse End Unit)",
    "House Style": "Style of dwelling (1Story=One story, 1.5Fin=One and one-half story finished, 2Story=Two story, SLvl=Split Level)",
    "Overall Qual": "Overall material and finish quality rating (1=Very Poor to 10=Very Excellent)",
    "Overall Cond": "Overall condition rating (1=Very Poor to 10=Very Excellent)",
    "Year Built": "Original construction year",
    "Year Remod/Add": "Remodel date (same as construction date if no remodeling or additions)",
    "Roof Style": "Type of roof (Flat, Gable, Gambrel, Hip, Mansard, Shed)",
    "Roof Matl": "Roof material (ClyTile=Clay or Tile, CompShg=Standard Composite Shingle, Membran=Membrane, Metal, Roll, Tar&Grv, WdShake, WdShngl)",
    "Exterior 1st": "Exterior covering on house (e.g., VinylSd=Vinyl Siding, MetalSd=Metal Siding, Wd Sdng=Wood Siding, HdBoard=Hard Board)",
    "Exterior 2nd": "Exterior covering on house (if more than one material)",
    "Mas Vnr Type": "Masonry veneer type (BrkCmn=Brick Common, BrkFace=Brick Face, CBlock=Cinder Block, Stone, None)",
    "Mas Vnr Area": "Masonry veneer area in square feet",
    "Exter Qual": "Exterior material quality (Ex=Excellent, Gd=Good, TA=Average/Typical, Fa=Fair, Po=Poor)",
    "Exter Cond": "Present condition of the material on the exterior (Ex=Excellent, Gd=Good, TA=Typical/Average, Fa=Fair, Po=Poor)",
    "Foundation": "Type of foundation (BrkTil=Brick & Tile, CBlock=Cinder Block, PConc=Poured Concrete, Slab, Stone, Wood)",
    "Bsmt Qual": "Height of the basement (Ex=Excellent (100+ inches), Gd=Good (90-99 inches), TA=Typical (80-89 inches), Fa=Fair (70-79 inches), Po=Poor (<70 inches), NA=No Basement)",
    "Bsmt Cond": "General condition of the basement (Ex=Excellent, Gd=Good, TA=Typical, Fa=Fair, Po=Poor, NA=No Basement)",
    "Bsmt Exposure": "Walkout or garden level basement walls (Gd=Good Exposure, Av=Average Exposure, Mn=Minimum Exposure, No=No Exposure, NA=No Basement)",
    "BsmtFin Type 1": "Quality of basement finished area (GLQ=Good Living Quarters, ALQ=Average Living Quarters, BLQ=Below Average Living Quarters, Rec=Average Rec Room, LwQ=Low Quality, Unf=Unfinished, NA=No Basement)",
    "BsmtFin SF 1": "Type 1 finished square feet",
    "BsmtFin Type 2": "Quality of second finished area (if present) (same ratings as BsmtFin Type 1)",
    "BsmtFin SF 2": "Type 2 finished square feet",
    "Bsmt Unf SF": "Unfinished square feet of basement area",
    "Total Bsmt SF": "Total square feet of basement area",
    "Heating": "Type of heating (Floor=Floor Furnace, GasA=Gas forced warm air furnace, GasW=Gas hot water or steam heat, Grav=Gravity furnace, OthW=Hot water or steam heat other than gas, Wall=Wall furnace)",
    "Heating QC": "Heating quality and condition (Ex=Excellent, Gd=Good, TA=Average/Typical, Fa=Fair, Po=Poor)",
    "Central Air": "Central air conditioning (N=No, Y=Yes)",
    "Electrical": "Electrical system (SBrkr=Standard Circuit Breakers & Romex, FuseA=Fuse Box over 60 AMP, FuseF=60 AMP Fuse Box, FuseP=60 AMP Fuse Box and mostly 3 AMP fuses, Mix=Mixed)",
    "1st Flr SF": "First floor square feet",
    "2nd Flr SF": "Second floor square feet",
    "Low Qual Fin SF": "Low quality finished square feet (all floors)",
    "Gr Liv Area": "Above grade (ground) living area square feet",
    "Bsmt Full Bath": "Basement full bathrooms",
    "Bsmt Half Bath": "Basement half bathrooms",
    "Full Bath": "Full bathrooms above grade",
    "Half Bath": "Half baths above grade",
    "Bedroom AbvGr": "Number of bedrooms above basement level",
    "Kitchen AbvGr": "Number of kitchens above grade",
    "Kitchen Qual": "Kitchen quality (Ex=Excellent, Gd=Good, TA=Typical/Average, Fa=Fair, Po=Poor)",
    "TotRms AbvGrd": "Total rooms above grade (does not include bathrooms)",
    "Functional": "Home functionality rating (Typ=Typical Functionality, Min1=Minor Deductions 1, Min2=Minor Deductions 2, Mod=Moderate Deductions, Maj1=Major Deductions 1, Maj2=Major Deductions 2, Sev=Severely Damaged, Sal=Salvage only)",
    "Fireplaces": "Number of fireplaces",
    "Fireplace Qu": "Fireplace quality (Ex=Excellent, Gd=Good, TA=Average, Fa=Fair, Po=Poor, NA=No Fireplace)",
    "Garage Type": "Garage location (2Types=More than one type, Attchd=Attached to home, Basment=Basement Garage, BuiltIn=Built-In, CarPort=Car Port, Detchd=Detached from home, NA=No Garage)",
    "Garage Yr Blt": "Year garage was built",
    "Garage Finish": "Interior finish of the garage (Fin=Finished, RFn=Rough Finished, Unf=Unfinished, NA=No Garage)",
    "Garage Cars": "Size of garage in car capacity",
    "Garage Area": "Size of garage in square feet",
    "Garage Qual": "Garage quality (Ex=Excellent, Gd=Good, TA=Typical/Average, Fa=Fair, Po=Poor, NA=No Garage)",
    "Garage Cond": "Garage condition (Ex=Excellent, Gd=Good, TA=Typical/Average, Fa=Fair, Po=Poor, NA=No Garage)",
    "Paved Drive": "Paved driveway (Y=Paved, P=Partial Pavement, N=Dirt/Gravel)",
    "Wood Deck SF": "Wood deck area in square feet",
    "Open Porch SF": "Open porch area in square feet",
    "Enclosed Porch": "Enclosed porch area in square feet",
    "3Ssn Porch": "Three season porch area in square feet",
    "Screen Porch": "Screen porch area in square feet",
    "Pool Area": "Pool area in square feet",
    "Pool QC": "Pool quality (Ex=Excellent, Gd=Good, TA=Average/Typical, Fa=Fair, NA=No Pool)",
    "Fence": "Fence quality (GdPrv=Good Privacy, MnPrv=Minimum Privacy, GdWo=Good Wood, MnWw=Minimum Wood/Wire, NA=No Fence)",
    "Misc Feature": "Miscellaneous feature not covered in other categories (Elev=Elevator, Gar2=2nd Garage, Othr=Other, Shed=Shed over 100 SF, TenC=Tennis Court, NA=None)",
    "Misc Val": "Dollar value of miscellaneous feature",
    "Mo Sold": "Month property was sold (1-12)",
    "Yr Sold": "Year property was sold",
    "Sale Type": "Type of sale (WD=Warranty Deed-Conventional, CWD=Warranty Deed-Cash, VWD=Warranty Deed-VA Loan, New=Home just constructed and sold, COD=Court Officer Deed/Estate, Con=Contract, ConLw=Contract Low Down, ConLI=Contract Low Interest, ConLD=Contract Low Down and Interest, Oth=Other)",
    "Sale Condition": "Condition of sale (Normal=Normal Sale, Abnorml=Abnormal Sale, AdjLand=Adjoining Land Purchase, Alloca=Allocation, Family=Sale between family members, Partial=Home was not completed when last assessed)",
    "SalePrice": "Property sale price in dollars (target variable for prediction)"
}

# Update descriptions
print("\nUpdating feature descriptions...")
updated_count = 0

for idx, row in df_dict.iterrows():
    feature_name = row['Feature']
    if feature_name in feature_descriptions:
        df_dict.at[idx, 'Description'] = feature_descriptions[feature_name]
        updated_count += 1

print(f"Updated {updated_count} feature descriptions")

# Save the updated data dictionary
output_path = "docs/data_dictionary.xlsx"
df_dict.to_excel(output_path, index=False, sheet_name='Data Dictionary')

print(f"\n[SUCCESS] Updated data dictionary saved to: {output_path}")
print(f"Total features documented: {len(df_dict)}")

# Display sample
print("\nSample of updated descriptions:")
print(df_dict[['Feature', 'Description']].head(10).to_string(index=False))