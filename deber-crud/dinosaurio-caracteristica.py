class Controller:
    filename="./"

    def __init__(self, filename):
        self.filename = filename
    
    def select(self, id):
        f = open(self.filename, "r")
        records = f.readlines()
        toReturn = []
        if(id == ""):
            for record in records:
                toReturn.append(record.rstrip().split(", "))
            return toReturn
        for record in records:
            toReturn = record.rstrip().split(", ")
            current_id = toReturn[0]
            if(current_id == id):
                return toReturn
        return []
    
    def insert(self, toWrite):
        text = ', '.join(str(value) for value in toWrite)
        f = open(self.filename, "a")
        f.write(text + "\n")

    def delete(self, id):
        f = open(self.filename, "r")
        records = f.readlines()
        f = open(self.filename, "w")
        for record in records:
            currentId = record.rstrip().split(", ")[0]
            if(currentId != id):
                f.write(record)

    def update(self, id, content):
        self.delete(id)
        self.insert(content)

class Dinosaur(Controller):

    id = 0
    name = ""
    height = 0.0   
    age = 0
    color = ""
    can_fly = False
	
    filename = "dinosaur.txt"

    def __init__(self, id = 0, name = "", height = "", age = 0, color = "", can_fly = False):
        super().__init__(self.filename)
        self.id = id
        self.name = name
        self.height = height
        self.age = age
        self.color = color
        self.can_fly = can_fly
    
    def select(self, id):
        result = super().select(id)
        if(id == ""):
            toReturn = []
            for value in result:
                toReturn.append(Dinosaur(value[0], value[1], value[2], value[3], value[4], value[5]))
        else:
            toReturn = Dinosaur(result[0], result[1], result[2], result[3], result[4], result[5])
        return toReturn

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.name}, Altura: {self.height}, Edad: {self.age}, Color: {self.color}, Puede volar?: {self.can_fly}"

class Feature(Controller):

    id = 0
    category = ""
    is_carnivouros = True
    weight = 0.0
    living_years = 0
    can_swim = False
    filename = "feature.txt"

    def __init__(self, id = 0, dinosaur = 0, category = "", is_carnivouros= True, weight = 0.0, living_years = 0, can_swim = False):
        super().__init__(self.filename)
        self.id = id
        self.dinosaur = dinosaur
        self.category = category
        self.is_carnivouros = is_carnivouros
        self.weight = weight
        self.living_years = living_years
        self.can_swim = can_swim
		
    def select(self, id, dinosaur):
        result = super().select(id)
        if(id == ""):
            toReturn = []
            for value in result:
                toReturn.append(Feature(value[0], value[1], value[2], value [3], value [4], value [5]))
            toReturn = self.filter(toReturn, dinosaur)
        else:
            if(result[1] == dinosaur):
                toReturn = Feature(result[0], result[1], result[2], result[3], result[4], result[5])
        return toReturn
    
    def filter(self, features_list, dinosaur):
        toReturn = []
        for feature in features_list:
            if(feature.dinosaur == dinosaur):
                toReturn. append(feature)
        return toReturn
    
    def __str__(self):
        return f"ID: {self.id}, dinosaurio: {self.dinosaur}, Categoría: {self.category}, Es carnívoro?: {self.is_carnivouros}, Peso: {self.weight}, Tiempo en la tierra: {self.living_years}, Puede nadar?: {self.can_swim}"

#consola
def max_id(items):
    max_value = 0
    for item in items:
        if(int(item.id) > max_value):
            max_value = int(item.id)
    return max_value


option = 0
dinosaurs_list = Dinosaur().select("")

while(option != "5"):
    print("Bienvenido al sistema de dinosaurios")
    print("1. Gestionar información de un dinosaurio")
    print("2. Ingresar dinosaurio")
    print("3. Eliminar dinosaurio")
    print("4. Mostrar dinosaurios")
    print("5. Salir")

    option = input("Seleccione una opción: ")
    if(option == "1"):

        dinosaur_option = 0
        dinosaur_id = input("Ingrese el ID de la dinosaurio: ")
        features_list = Feature().select("", dinosaur_id)

        while(dinosaur_option != "7"):
            print("1. Editar información del dinosaurio")
            print("2. Ver características")
            print("3. Eliminar característica")
            print("4. Buscar característica")
            print("5. Insertar característica")
            print("6. Editar característica")
            print("7. Atras")
            dinosaur_option = input("Seleccione una opción: ")
            if(dinosaur_option == "1"):
                name = input("Ingrese el nuevo nombre del dinosaurio: ")
                height = input("La nueva altura es: ")
                age = input("La nueva edad es: ")
                color = input("El nuevo color es: ")
                can_fly = input("Puede volar? (True/False) ")
                dinosaurs_list[0].update(dinosaur_id, [dinosaur_id, name, height, age, color, can_fly])
            elif(dinosaur_option == "2"):
                features_list = Feature().select("", dinosaur_id)
                for feature in features_list:
                    print(feature)
            elif(dinosaur_option == "3"):
                to_delete = input("Ingrese el ID de la característica: ")
                features_list[0].delete(to_delete)
            elif(dinosaur_option == "4"):
                to_select = input("Ingrese el ID del característica: ")
                feature = features_list[0].select(to_select, dinosaur_id)
                print(feature)
            elif(dinosaur_option == "5"):
                new_id = str(max_id(features_list) + 1)
                category = input("Ingrese la nueva categoría: ")
                is_carnivorus = input("Es carnívoro? (True/False) : ")
                weight = input("El nuevo peso es: ")
                living_years = input("Cuánto tiempo lleva en la tierra? ")
                can_swim = input("Puede nadar? (True/False) ")
                feature().insert([new_id, dinosaur_id, category, is_carnivorus, weight, living_years, can_swim])
            elif(dinosaur_option == "6"):
                feature_id = input("Ingrese el ID de la característica: ")
                category = input("Ingrese la nueva categoría: ")
                is_carnivorus = input("Es carnívoro? (True/False): ")
                weight = input("El nuevo peso es: ")
                living_years = input("Cuánto tiempo lleva en la tierra? ")
                can_swim = input("Puede nadar? (True/False) ")
                features_list[0].update(feature_id, [feature_id, dinosaur_id, category, is_carnivorus, weight, living_years, can_swim])
    elif(option == "2"):
        dinosaur_id = str(max_id(dinosaurs_list) + 1)
        name = input("Ingrese el nuevo nombre del dinosaurio: ")
        height = input("La nueva altura es: ")
        age = input("La nueva edad es: ")
        color = input("El nuevo color es: ")
        can_fly = input("Puede volar? (True/False) ")
        dinosaurs_list[0].insert([dinosaur_id, name, height, age, color, can_fly])
        dinosaurs_list = dinosaurs_list[0].select("")
    elif(option == "3"):
        dinosaur_id = input("Ingrese el ID de la dinosaurio: ")
        dinosaurs_list[0].delete(dinosaur_id)
        dinosaurs_list = dinosaurs_list[0].select("")
    elif(option == "4"):
        for dinosaur in dinosaurs_list:
            print(dinosaur)



