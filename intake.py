from intake_stac import StacCatalog, StacCollection, StacItem
import intake

cat = StacCatalog('/Users/wwatkins/test/catalog.json')
item = cat['GCM4_MRI_sund_1990to1999']
item_dask = item.to_dask() #need to get plugin recognized here


