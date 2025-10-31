class Pila:
    def __init__(self):
        """Inicializa una pila vacía."""
        self.items = []
    
    def push(self, item):
        """Agrega un elemento a la cima de la pila."""
        self.items.append(item)
        print(f"→ Push: '{item}' agregado a la pila.")
    
    def pop(self):
        """Quita y devuelve el elemento en la cima de la pila."""
        if not self.esta_vacia():
            item = self.items.pop()
            print(f"← Pop: '{item}' eliminado de la pila.")
            return item
        else:
            print("¡Error! La pila está vacía. No se puede hacer pop.")
            return None
    
    def peek(self):
        """Devuelve el elemento en la cima sin eliminarlo."""
        if not self.esta_vacia():
            return self.items[-1]
        else:
            print("¡La pila está vacía! No hay cima.")
            return None
    
    def esta_vacia(self):
        """Devuelve True si la pila está vacía."""
        return len(self.items) == 0
    
    def tamano(self):
        """Devuelve el número de elementos en la pila."""
        return len(self.items)
    
    def mostrar(self):
        """Muestra todos los elementos de la pila (de abajo hacia arriba)."""
        if self.esta_vacia():
            print("Pila: [] (vacía)")
        else:
            print(f"Pila: {self.items}  ← (cima)")
    
    def vaciar(self):
        """Elimina todos los elementos de la pila."""
        self.items.clear()
        print("Pila vaciada.")


# ========================================
# EJEMPLO DE USO
# ========================================
if __name__ == "__main__":
    print("=== DEMO DE PILA EN PYTHON ===\n")
    
    pila = Pila()
    
    # Agregar elementos
    pila.push("Manzana")