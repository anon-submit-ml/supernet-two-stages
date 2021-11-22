BASELINE_RUNS_CIFAR10 = [
    #('none', 10, '00000000-000000'),
    #('none', 11, '00000000-000000'),
    #('none', 12, '00000000-000000'),
    #('rsps', 10, '20210925-002854'),
    #('rsps', 11, '20210925-002903'),
    #('rsps', 12, '20210925-004412'),
    #('rsps+', 10, '20210925-005917'),
    #('rsps+', 11, '20210925-005933'),
    #('rsps+', 12, '20210925-005938')
    ('none+', 10, '20211003-051126'),
    ('none+', 11, '20211003-051127'),
    ('none+', 12, '20211003-053116'),
]

BASELINE_RUNS_CIFAR100 = [
    #('none', 10, '00000000-000000'),
    #('none', 11, '00000000-000000'),
    #('none', 12, '00000000-000000'),
    #('rsps', 10, '20210925-005938'),
    #('rsps', 11, '20210925-012351'),
    #('rsps', 12, '20210925-012401'),
    #('rsps+', 10, '20210925-052103'),
    #('rsps+', 11, '20210925-052112'),
    #('rsps+', 12, '20210925-052131')
    ('none+', 10, '20211003-053739'),
    ('none+', 11, '20211003-055017'),
    ('none+', 12, '20211003-055207'),
]

BASELINE_RUNS_IMAGENET = [
    #('none', 10, '00000000-000000'),
    #('none', 11, '00000000-000000'),
    #('none', 12, '00000000-000000'),
    #('rsps2', 10, '20211025-224608'),
    #('rsps2', 11, '20211025-224609'),
    #('rsps2', 12, '20211025-224633'),
    #('rsps+', 10, '20211025-224608'),
    #('rsps+', 11, '20211025-224609'),
    #('rsps+', 12, '20211025-224633'),
    ('none+', 10, '20211003-055305'),
    ('none+', 11, '20211003-055329'),
    ('none+', 12, '20211003-055403'),
]


EXP_RUNS_CIFAR10 = [
    ('darts', 10, '20210925-000717'),
    ('darts', 11, '20210925-000726'),
    ('darts', 12, '20210925-001154'),
    ('darts-', 10, '20211003-030441'),
    ('darts-', 11, '20211003-032009'),
    ('darts-', 12, '20211003-034111'),
    ('gdas', 10, '20210925-004414'),
    ('gdas', 11, '20210925-004414'),
    ('gdas', 12, '20210925-004412'),
    ('snas', 10, '20210924-235517'),
    ('snas', 11, '20210925-000350'),
    ('snas', 12, '20210925-000551'),
    ('dirichlet', 10, '20210930-014925'),
    ('dirichlet', 11, '20210930-014934'),
    ('dirichlet', 12, '20210930-014942')
]

EXP_RUNS_50_CIFAR10 = [
    ('darts', 10, '20211025-050130'),
    ('darts', 11, '20211025-050138'),
    ('darts', 12, '20211025-050239'),
    ('darts-', 10, '20211025-141050'),
    ('darts-', 11, '20211025-141242'),
    ('darts-', 12, '20211025-141554'),
    ('gdas', 10, '20211025-050103'),
    ('gdas', 11, '20211025-050120'),
    ('gdas', 12, '20211025-050125'),
    ('snas', 10, '20211025-050026'),
    ('snas', 11, '20211025-050026'),
    ('snas', 12, '20211025-050032'),
    ('dirichlet', 10, '20211025-051349'),
    ('dirichlet', 11, '20211025-051354'),
    ('dirichlet', 12, '20211025-075629')
]

EXP_RUNS_250_CIFAR10 = [
    ('darts', 10, '20211025-045834'),
    ('darts', 11, '20211025-045852'),
    ('darts', 12, '20211025-045903'),
    ('darts-', 10, '20211025-141721'),
    ('darts-', 11, '20211025-142309'),
    ('darts-', 12, '20211025-142807'),
    ('gdas', 10, '20211025-045825'),
    ('gdas', 11, '20211025-045817'),
    ('gdas', 12, '20211025-045832'),
    ('snas', 10, '20211025-045749'),
    ('snas', 11, '20211025-045751'),
    ('snas', 12, '20211025-045809'),
    ('dirichlet', 10, '20211025-050006'),
    ('dirichlet', 11, '20211025-050008'),
    ('dirichlet', 12, '20211025-050023')
]

EXP_RUNS_CIFAR100 = [
    ('darts', 10, '20210925-052154'),
    ('darts', 11, '20210925-052210'),
    ('darts', 12, '20210925-052214'),
    ('darts-', 10, '20211003-034138'),
    ('darts-', 11, '20211003-034445'),
    ('darts-', 12, '20211003-034834'),
    ('gdas', 10, '20210925-055119'),
    ('gdas', 11, '20210925-055323'),
    ('gdas', 12, '20210925-055640'),
    ('snas', 10, '20210925-054004'),
    ('snas', 11, '20210925-054013'),
    ('snas', 12, '20210925-054808'),
    ('dirichlet', 10, '20210930-014947'),
    ('dirichlet', 11, '20210930-015002'),
    ('dirichlet', 12, '20210930-015027')
]

EXP_RUNS_50_CIFAR100 = [
    ('darts', 10, '20211026-022143'),
    ('darts', 11, '20211026-022548'),
    ('darts', 12, '20211026-041445'),
    ('darts-', 10, '20211026-041553'),
    ('darts-', 11, '20211026-042645'),
    ('darts-', 12, '20211026-044939'),
    ('gdas', 10, '20211025-231808'),
    ('gdas', 11, '20211025-231939'),
    ('gdas', 12, '20211025-233044'),
    ('snas', 10, '20211025-230956'),
    ('snas', 11, '20211025-231248'),
    ('snas', 12, '20211025-231711'),
    ('dirichlet', 10, '20211025-234329'),
    ('dirichlet', 11, '20211025-234329'),
    ('dirichlet', 12, '20211026-021855')
]

EXP_RUNS_250_CIFAR100 = [
    ('darts', 10, '20211025-045039'),
    ('darts', 11, '20211025-045039'),
    ('darts', 12, '20211025-045327'),
    ('darts-', 10, '20211025-143424'),
    ('darts-', 11, '20211025-143424'),
    ('darts-', 12, '20211025-165938'),
    ('gdas', 10, '20211025-044743'),
    ('gdas', 11, '20211025-044906'),
    ('gdas', 12, '20211025-044918'),
    ('snas', 10, '20211025-044643'),
    ('snas', 11, '20211025-044643'),
    ('snas', 12, '20211025-044730'),
    ('dirichlet', 10, '20211025-045617'),
    ('dirichlet', 11, '20211025-045644'),
    ('dirichlet', 12, '20211025-045644')
]

EXP_RUNS_IMAGENET = [
    ('darts', 10, '20210930-014448'),
    ('darts', 11, '20210930-014504'),
    ('darts', 12, '20210930-014530'),
    ('darts-', 10, '20210925-055647'),
    ('darts-', 11, '20210925-055647'),
    ('darts-', 12, '20210925-055647'),
    ('gdas', 10, '20210930-014712'),
    ('gdas', 11, '20210930-014747'),
    ('gdas', 12, '20210930-014750'),
    ('snas', 10, '20210930-014654'),
    ('snas', 11, '20210930-014703'),
    ('snas', 12, '20210930-014709'),
    ('dirichlet', 10, '20210930-014849'),
    ('dirichlet', 11, '20210930-014911'),
    ('dirichlet', 12, '20210930-014912')
]

EXP_RUNS_DS_CIFAR10 = [
    #('darts', 10, '20210927-083153'),
    #('darts', 11, '20211001-035434'),
    #('darts', 12, '20211001-035434'),
    #('darts-', 10, '20210927-100227'),
    ('darts-', 11, '20211116-172829'),
    ('darts-', 12, '20211116-173302'),
    #('gdas', 10, '20211002-035454'),
    #('gdas', 11, '20211107-152333'),
    #('gdas', 12, '20211107-152459'),
    #('snas', 10, '20210927-090547'),
    #('snas', 11, '20211001-035452'),
    #('snas', 12, '20211001-035509'),
    #('dirichlet', 10, '20211001-035534'),
    #('dirichlet', 11, '20211001-035554'),
    #('dirichlet', 12, '20211001-035602')
]

EXP_RUNS_DS_CIFAR100 = [
    ('darts', 10, '20211001-040103'),
    #('darts', 11, '20211001-041321'),
    #('darts', 12, '20211001-041328'),
    ('darts-', 10, '20211002-033331'),
    #('darts-', 11, '20211109-163413'),
    #('darts-', 12, '20211109-163432'),
    ('gdas', 10, '20211002-040535'),
    #('gdas', 11, '20211109-163820'),
    #('gdas', 12, '20211109-163827'),
    ('snas', 10, '20211001-041341'),
    #('snas', 11, '20211001-041404'),
    #('snas', 12, '20211001-041412'),
    ('dirichlet', 10, '20211001-041433'),
    #('dirichlet', 11, '20211001-041443'),
    #('dirichlet', 12, '20211001-041452')
]

EXP_RUNS_100_DS_CIFAR10 = [
    ('darts', 10, '20211116-164305'),
    ('darts', 11, '20211116-164305'),
    ('darts', 12, '20211116-164305'),
    ('darts-', 10, '20211116-164316'),
    ('darts-', 11, '20211116-164334'),
    ('darts-', 12, '20211116-164334'),
    ('gdas', 10, '20211116-173435'),
    ('gdas', 11, '20211116-173434'),
    ('gdas', 12, '20211116-173443'),
    ('snas', 10, '20211116-173350'),
    ('snas', 11, '20211116-173350'),
    ('snas', 12, '20211116-173350'),
    ('dirichlet', 10, '20211116-173457'),
    ('dirichlet', 11, '20211116-173504'),
    ('dirichlet', 12, '20211116-173512')
]

DARTSM_DS_NO_DECAY = [
    ('cifar10', 10, '20211002-034511'),
    ('cifar10', 11, '20211109-170426'),
    ('cifar10', 12, '20211109-170428'),
    ('cifar100', 10, '20211002-034520'),
    ('cifar100', 11, '20211109-170444'),
    ('cifar100', 12, '20211109-170452')
]

DARTSM_CIFAR = [
    (10, '20211003-030441', 'cifar10', 'none'),
    (11, '20211003-032009', 'cifar10', 'none'),
    (12, '20211003-034111', 'cifar10', 'none'),
    (10, '20211003-034138', 'cifar100', 'none'),
    (11, '20211003-034445', 'cifar100', 'none'),
    (12, '20211003-034834', 'cifar100', 'none'),
    (10, '20211003-050428', 'cifar10', 'linear'),
    (11, '20211003-050435', 'cifar10', 'linear'),
    (12, '20211003-050442', 'cifar10', 'linear'),
    (10, '20211003-050304', 'cifar100', 'linear'),
    (11, '20211003-050313', 'cifar100', 'linear'),
    (12, '20211003-050320', 'cifar100', 'linear')
]

DARTSM_IMAGENET = [
    (10, '20211003-035406', 'none'),
    (11, '20211003-035652', 'none'),
    (12, '20211003-035814', 'none'),
    (10, '20211003-050231', 'linear'),
    (11, '20211003-050241', 'linear'),
    (12, '20211003-050249', 'linear')
]

BASELINE_2 = [
    #('rsps', 10, '20211004-090335', 'cifar10'),
    #('rsps', 11, '20211004-090345', 'cifar10'),
    #('rsps', 12, '20211004-090355', 'cifar10'),
    #('rsps+', 10, '20211004-130941', 'cifar10'),
    #('rsps+', 11, '20211004-130953', 'cifar10'),
    #('rsps+', 12, '20211004-131003', 'cifar10'),
    ('rsps', 10, '20211004-090409', 'cifar100'),
    ('rsps', 11, '20211004-090418', 'cifar100'),
    ('rsps', 12, '20211004-090427', 'cifar100'),
    #('rsps+', 10, '20211004-131020', 'cifar100'),
    #('rsps+', 11, '20211004-131027', 'cifar100'),
    #('rsps+', 12, '20211004-131035', 'cifar100')
]

RSPS2 = [
    ('rsps2', 10, '20211004-130941', 'cifar10'),
    ('rsps2', 11, '20211004-130953', 'cifar10'),
    ('rsps2', 12, '20211004-131003', 'cifar10'),
    ('rsps2', 10, '20211004-131020', 'cifar100'),
    ('rsps2', 11, '20211004-131027', 'cifar100'),
    ('rsps2', 12, '20211004-131035', 'cifar100')
]
