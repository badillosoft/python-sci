import vtk

# Modelo (Source)
cilindro = vtk.vtkCylinderSource()
cilindro.SetResolution(20)

# Mapeador: Modelo -> Escena
cilindroMapper = vtk.vtkPolyDataMapper()
cilindroMapper.SetInputConnection(cilindro.GetOutputPort())

# Actor: Controla el modelo en la escena
cilindroActor = vtk.vtkActor()
cilindroActor.SetMapper(cilindroMapper)
cilindroActor.RotateX(45)

# Renderer: Dibuja en la escena
ren = vtk.vtkRenderer()
ren.AddActor(cilindroActor)
ren.ResetCamera()
#ren.GetActiveCamera().Zoom(1.5)

# Ventana
win = vtk.vtkRenderWindow()
win.AddRenderer(ren)
win.SetSize(600, 400)

# Interactor: Interactua el usuario con la ventana
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(win)
interactor.Initialize()

# Proceso de comienzo
win.Render()
interactor.Start()