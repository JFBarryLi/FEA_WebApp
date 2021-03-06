import logging
import numpy as np

log = logging.getLogger(__name__)


class Element():
    """
    Element class, represent a bar element with circular/tubular cross-section.

    ...

    Attributes
    ----------
    id : str
        Id for the element.
    index : int
        Index of the element.
    nodei : Node
        Node object, representing node i.
    nodej : Node
        Node object, representing node j.
    E : float
        Young's modulus [MPa].
    A : float
        Cross sectional area of the element [mm^2].
    L : float
        Length of the element.
    Cx : float
        Direction cosine in x.
    Cy : float
        Direction cosine in y.
    Cz : float
        Direction cosine in z.
    K : ndarray
        Stiffness matrix for the element in global coordinates.

    Methods
    -------
    stiffness()
        Compute the stiffness matrix for the element in global coordinates.

    """

    def __init__(self, id, index, nodei, nodej, mat_prop):
        self.id = id
        self.index = index
        self.nodei = nodei
        self.nodej = nodej
        self.E = mat_prop['E']
        self.A = mat_prop['A']

        # Calculated element properties.
        log.debug(f'Calculating element[{self.id}] length.')
        self.L = np.linalg.norm((
            nodej.x - nodei.x,
            nodej.y - nodei.y,
            nodej.z - nodei.z
        ))

        log.debug(f'Calculating element[{self.id}] direction cosines.')
        self.Cx = (self.nodej.x - self.nodei.x) / self.L
        self.Cy = (self.nodej.y - self.nodei.y) / self.L
        self.Cz = (self.nodej.z - self.nodei.z) / self.L

    def stiffness(self):
        E = self.E
        A = self.A
        L = self.L
        Cx = self.Cx
        Cy = self.Cy
        Cz = self.Cz

        log.debug(f'Calculating element[{self.id}] stiffness matrix.')
        self.K = E * A / L * np.array([
            [ Cx**2,  Cx*Cy,  Cx*Cz, -Cx**2, -Cx*Cy, -Cx*Cz],  # noqa: E201
            [ Cx*Cy,  Cy**2,  Cy*Cz, -Cx*Cy, -Cy**2, -Cy*Cz],  # noqa: E201
            [ Cx*Cz,  Cy*Cz,  Cz**2, -Cx*Cz, -Cy*Cz, -Cz**2],  # noqa: E201
            [-Cx**2, -Cx*Cy, -Cx*Cz,  Cx**2,  Cx*Cy,  Cx*Cz],  # noqa: E201
            [-Cx*Cy, -Cy**2, -Cy*Cz,  Cx*Cy,  Cy**2,  Cy*Cz],  # noqa: E201
            [-Cx*Cz, -Cy*Cz, -Cz**2,  Cx*Cz,  Cy*Cz,  Cz**2],  # noqa: E201
        ])
