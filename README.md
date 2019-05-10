# Products API (Python Docker) 

Technological Institute of Costa Rica
Project2 CompraTec
Teacher: Raul Madrigal Acuña
Students: Raul Arias, Rony Paniagua
Script docker swarm

## Products model

>name: string
>code: int
>cost: int
>amount: int

## API usage

### Consult
To consult the products, the following query is used: 
```
{
  GetProducts(code:1){
    name code cost amount
  }
}
```
Where you can use any parameter, none or all those specified in the model.

### Insert
To insert the products the following mutation is used:
```
mutation{
  createProduct(name: "test2", amount: 2, cost: 2, code: 2){
    product {
      id name
    }
  }
}
```
Where in the result you can consult any of the attributes of the created product.

### Update
To update the products the following mutation is used:
```
mutation{
  updateProductCost(name: "Test", code:1, cost:1){
    product{
      name
    }
  }
}
```
Where the name and code of the product is received as parameters to modify the cost, and in the result you can consult any of the attributes of the updated product.

## Delete
To delete the products the following mutation is used:
```
mutation{
  deleteProduct(code:1 ){
    product{
      name
    }
  }
}
```
Where the code of the product to be deleted is received as a parameter, and in the result you can consult any of the attributes of the deleted product.
