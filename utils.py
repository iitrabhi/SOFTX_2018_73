import dolfin as dlf

def load_mesh(mesh_file):
    """
    Load the mesh file specified by the user. The file may be
    xml, or HDF5 (assuming the current dolfin installation
    has the support).


    Parameters
    ----------

    mesh_file : str
        Name of the file that contains the desired mesh information.


    Returns
    -------

    mesh : dolfin.cpp.mesh.Mesh
        This function returns a dolfin mesh object.


    """

    if mesh_file[-3:] == '.h5':
        mesh = __load_mesh_hdf5(mesh_file)
    else:
        mesh = dlf.Mesh(mesh_file)

    return mesh


def load_mesh_function(mesh_function, mesh):
    """
    Load the mesh function file specified by the user. The file may be
    xml, or HDF5 (assuming the current dolfin installation
    has the support).

    Parameters
    ----------

    mesh_function : str
        Name of the file that contains the desired mesh function information.

    mesh : dolfin.cpp.mesh.Mesh
        The dolfin mesh object that corresponds to the mesh function.


    Returns
    -------

    mesh_func : dolfin.cpp.mesh.MeshFunctionSizet
        This function returns a dolfin mesh function object.


    """

    if mesh_function[-3:] == '.h5':
        mesh_func = __load_mesh_function_hdf5(mesh_function, mesh)
    else:
        mesh_func = dlf.MeshFunction('size_t', mesh, mesh_function)

    return mesh_func


def __load_mesh_hdf5(mesh_file):
    """
    Load dolfin mesh from an HDF5 file.

    Parameters
    ----------

    mesh_file : str
        Name of the file containing the mesh information


    Returns
    -------

    mesh : dolfin.cpp.mesh.Mesh
        This function returns a dolfin mesh object.

    """

    # Check dolfin for HDF5 support
    if not dlf.has_hdf5():
        s1 = 'The current installation of dolfin does not support HDF5 files.'
        raise Exception(s1)

    # Check file extension
    if mesh_file[-3:] == '.h5':
        f = dlf.HDF5File(dlf.mpi_comm_world(), mesh_file, 'r')
        mesh = dlf.Mesh()
        f.read(mesh, 'mesh', False)
        f.close()
    else:
        s1 = 'The file extension provided must be \'.h5\'.'
        raise ValueError(s1)

    return mesh


def __load_mesh_function_hdf5(mesh_function, mesh):
    """
    Load a dolfin mesh function from an HDF5 file.

    Parameters
    ----------

    mesh_function : str
        Name of the file containing the mesh function information


    Returns
    -------

    mesh_func : dolfin.cpp.mesh.MeshFunctionSizet
        This function returns a dolfin mesh function object.

    """

    # Check dolfin for HDF5 support
    if not dlf.has_hdf5():
        s1 = 'The current installation of dolfin does not support HDF5 files.'
        raise Exception(s1)

    # Check file extension
    if mesh_function[-3:] == '.h5':
        f = dlf.HDF5File(dlf.mpi_comm_world(), mesh_function, 'r')
        mesh_func = dlf.MeshFunction('size_t', mesh)
        f.read(mesh_func, 'mesh_function')
        f.close()
    else:
        s1 = 'The file extension provided must be \'.h5\'.'
        raise ValueError(s1)

    return mesh_func
