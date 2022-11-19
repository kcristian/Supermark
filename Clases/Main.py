from producto import Producto
from categoria import Categoria
from Detalle_compra import DetalleCompra
from roles import Rol
from usuario import Usuario
from datetime import date
def main():
    print("hola")
    #f=date(2022,12,10)
    #c=Categoria(1,"cereal")
    #p=Producto(10,"arroz perseguido 500 gr",120,200,c,f)
    #detalle=DetalleCompra(p,7)
    #print(detalle)

    mi_rol=Rol.STAFF
    print(mi_rol)
    print(mi_rol.value)
if __name__=="__main__":
    main()