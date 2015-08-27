# coding=utf-8
from Arboles import Nodo
# Recuerda borrar los 'pass'. Pudes borrar si quieres los comentarios.


class Commit:
    commits = 0
    def __init__(self, message, changes):
        Commit.commits += 1
        self.message = message
        self.changes = changes
        self.ide = Commit.commits
        #############
        # COMPLETAR:
        # 'changes' es una lista de tuplas.
        # Puedes modificar esta clase a gusto tuyo.
        #############

class Branch(Nodo):
    def __init__(self,padre,nombre):
        self.padre = padre
        self.commits = []
        self.valor = nombre
        self.files = ['.jit']
        self.hijos = []
    #############
    # COMPLETAR:
    # Crear __init__ con lo que consideres necesario
    #############

    def add_hijos(self,lista):
        #lista es una lista de nodos o
        #lista tambien puede poseer valores y estos serán transformados en nodos
        try:
            for hijo in lista:
                if str(type(hijo))[17:-2] == "Branch":
                    self.hijos.append(hijo)
                else:
                    self.hijos.append(Branch(hijo,self.valor))
        except:
            print("Error")

    def new_commit(self, commit):
        A = False
        for File in commit.changes:
            if File[0] == 'CREATE':
                if not File[1] in self.files:
                    self.files.append(File[1])
                    A = True
            elif File[0] == 'DELETE':
                if File[1] in self.files:
                    self.files.pop(self.files.index(File[1]))
                    A = True
        if A:
            self.commits.append(commit)

        #############
        # COMPLETAR:
        # Agregar un nuevo commit del tipo Commit a esta branch.
        # Este commit define el estado final temporalmente.
        #############


    def pull(self):
        files = self.files
        #############
        # COMPLETAR:
        # Retornar el estado final de esta branch (una lista de archivos).
        #############
        return files

    def checkout(ide):
        files = set()
        for branch in self.hijos:
            for commit in branch.commits:
                if commit.ide <= ide:
                    for xfile in branch.files:
                        files.add(xfile)

            files.union(branch.checkout)
        return files


class Repository:

    def __init__(self, name):
        self.name = name
        self.master = Branch(None,'master')
        self.commits = 0
        #############
        # COMPLETAR:
        # Crear branch 'master'.
        # Crear commit inicial y agregarlo a 'master'.
        #############

    def create_branch(self, new_branch_name, from_branch_name):
        self.master.add_hijos([Branch(from_branch_name,new_branch_name)])
        #############
        # COMPLETAR:
        # Crear branch a partir del último estado de la 'from_branch_name'.
        #############


    def branch(self, branch_name):
        return self.master.subnodo(branch_name)

    def checkout(self, commit_id):
        return list(self.master.checkout(commit_id))
            
        #############
        # COMPLETAR:
        # Buscar el commit con cierta id y retornar el estado del repositorio
        # hasta ese commit. Puede estar en cualquier branch.
        #############
        


if __name__ == '__main__':
    # Ejemplo de uso
    # Puedes modificarlo para probar esto pero al momento de la corrección
    # el ayudante borrará cualquier cambio y restaurará las siguientes lineas
    # a su estado original (como se muestran aquí).

    repo = Repository("syllabus 2.0")

    repo.branch("master").new_commit(Commit(
        message="agregado readme",
        changes=[("CREATE", "README.md")]
    ))

    repo.branch("master").new_commit(Commit(
        message="archivos base",
        changes=[("CREATE", "main.py"), ("CREATE", "clases.py")]
    ))

    # Creamos una rama del estado actual de 'master'
    repo.create_branch("desarrollo-de-vistas", 'master')
    repo.branch("desarrollo-de-vistas").new_commit(Commit(
        message="imagenes",
        changes=[("CREATE", "main.jpg"), ("CREATE", "user.png")]
    ))

    repo.branch("desarrollo-de-vistas").new_commit(Commit(
        message="cambiar instrucciones",
        changes=[("DELETE", "README.md"), ("CREATE", "instrucciones.html")]
    ))

    repo.branch("master").new_commit(Commit(
        message="datos recolectados",
        changes=[("CREATE", "data.csv")]
    ))

    print(repo.branch("master").pull())
    # Esperamos que el repo esté así:
    # ['.jit', 'README.md', 'main.py', 'clases.py', 'data.csv']

    print(repo.branch("desarrollo-de-vistas").pull())
    # Esperamos que el repo esté así:
    # ['.jit', 'main.py', 'clases.py',
    #  'main.jpg', 'user.png', 'instrucciones.html']

    print(repo.checkout(4))
    # Esperamos que el repo esté así:
    # ['.jit', 'README.md', 'main.py', 'clases.py', 'main.jpg', 'user.png']

    print(repo.checkout(1))
    # Esperamos que el repo esté así:
    # ['.jit']
