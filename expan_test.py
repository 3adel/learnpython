from expan.core.util import generate_random_data
from expan.core.experiment import Experiment
from expan.core.statistical_test import KPI, Variants, StatisticalTest


data, metadata = generate_random_data()

print(data.head())
print(metadata)


kpi = KPI('normal_same')
variants = Variants(variant_column_name='variant', control_name='B', treatment_name='A')
test = StatisticalTest(data=data, kpi=kpi, features=[], variants=variants)
exp = Experiment(metadata=metadata)

result = exp.analyze_statistical_test(test)

print(result)