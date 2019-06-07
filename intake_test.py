from intake_stac import StacCatalog,StacCollection, StacItem

cat = StacCatalog('catalog.json')
print(list(cat))
item=cat['test_netcdf']
print(item)
item_dask = item.to_dask() #need to get plugin recognized here


