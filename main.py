from curtis import CurtisEngine, CurtisFact
from curtis.utils.encoding import diagnosis_indexes

engine = CurtisEngine()

engine.declare_fact(
    CurtisFact(
        sex=1,
        age=89,
        height=140,
        weight=30,
        HR=56,
        Pd=122,
        PQ=164,
        QRS=118,
        QT=460,
        QTcFra=451
    )
)

diagnosis = engine.diagnose()

print(diagnosis_indexes[diagnosis])
