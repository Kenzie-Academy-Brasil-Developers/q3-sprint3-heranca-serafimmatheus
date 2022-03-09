from classes import Recipiente, Copo

if __name__ == "__main__":
    # Execute suas testagens manuais aqui


    r = Recipiente(100)
    print(r)
    r.esta_limpo()
    print(r.estado())
    r.sujar()
    r.esta_limpo()
    r.lavar()
    r.esta_limpo()

    c = Copo(300)
    print(c)
    c.encher("Café")
    print(c.bebida)
    print(c)
    c.beber(30)
    print(c)
    c.lavar()
    c.esta_limpo()
