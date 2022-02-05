# CFDprj

Politecnico di Milano [computational fluid dynamics project](https://www4.ceda.polimi.it/manifesti/manifesti/controller/ManifestoPublic.do?EVN_DETTAGLIO_RIGA_MANIFESTO=evento&aa=2021&k_cf=225&k_corso_la=469&k_indir=AER&codDescr=051176&lang=IT&semestre=1&idGruppo=4396&idRiga=275024). 

This repository stores all the cases relative to the course assignment that are solved with [OpenFOAM](https://github.com/OpenFOAM/OpenFOAM-9). 

## Course assignment

The course assignment consists of 5 laboratories that have different subcases. 

|Case          | Mesh | Description         | Subcases |
| ---          | ---  | ---                 | --- |
|Lab02         | 2D   | Incompressible flow | simpleFoam <br /> pimpleFoamCFL1 <br /> pimpleFoamCLF15 | 
|Lab04         | 2D   | Compressible flow   | rhoPimpleFoam<sub>(highT, highRe)</sub> <br /> rhoPimpleFoam<sub>(highT, lowRe)</sub> <br /> rhoPimpleFoam<sub>(lowT, lowRe)</sub> |
|Lab05-06      | 2D   | Spray \& wall-film  | reactingFoam<sub>ReitzDiwakar</sub> <br /> reactingFoam<sub>ReitzKHRT</sub> <br /> reactingFoam<sub>ReitzKHRT450</sub> |
|Lab07         | 2D   | Reactive flow <br /> CH<sub>4</sub> combustion               | rhoPimpleFoam <br /> reactingFoam |
|LabAssignment | 3D   | Reactive flow <br /> C<sub>7</sub> H<sub>16</sub> combustion | rhoPimpleFoam <br /> reactingFoam |

All the cases have a `script/` folder that stores `latexData.py` script for data extraction and plotting.

