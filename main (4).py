def linearSearchProduct(productlist,targetproduct):
  indices=[]
  for index, product in enumerate(productlist):
    if product == targetproduct:
      indices.append(index)
  return indices


#example usage
products =["shoes","boot","sandal","shoes","loafer","shoes"]
target = "shoes"
target2="apple"
result = linearSearchProduct(products,target)
print(result)