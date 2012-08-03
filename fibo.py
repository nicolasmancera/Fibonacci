if __name__ == '__main__':

         print("Cadenas de fibonacci")
         print("Cuantos numeros de la serie quiere calcular "),

         n = int(raw_input())
         fib1,fib2 = 0,1

         for i in range(n):
             fib1, fib2 = fib2, fib1 + fib2
             print(fib2),

         print("\nFin del programa")
         print("Gracias.")
         raw_input() 
