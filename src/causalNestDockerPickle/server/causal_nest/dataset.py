from typing import List, Dict, Any, Optional
import networkx as nx


def create_mock_graph():
    """
    Creates a mock directed graph using NetworkX.
    """
    graph = nx.DiGraph()
    graph.add_node("displacement", label="displacement\n-0.05", fillcolor="lightpink")
    graph.add_node(
        "cylinders", label="cylinders\n0.00", fillcolor="gray", shape="doublecircle"
    )
    graph.add_node("weight", label="weight\n-0.01", fillcolor="lightpink")
    graph.add_node(
        "modelyear", label="modelyear\n0.72", fillcolor="#4CAF50", fontcolor="white"
    )
    graph.add_node("horsepower", label="horsepower\n-0.11", fillcolor="lightpink")
    graph.add_node(
        "acceleration",
        label="acceleration\n0.00",
        fillcolor="gray",
        shape="doublecircle",
    )
    graph.add_node(
        "origin", label="origin\n0.42", fillcolor="#4CAF50", fontcolor="white"
    )
    graph.add_node(
        "mpg",
        label="mpg",
        fillcolor="magenta",
        color="purple",
        shape="hexagon",
        fontcolor="white",
    )


# Define the dataset feature mapping, target, and the problem
class MissingDataHandlingMethod:
    FORWARD_FILL = "forward_fill"
    FORWARD_INTERPOLATION = "forward_interpolation"
    DROP = "drop"


class FeatureType:
    CONTINUOUS = "continuous"
    DISCRETE = "discrete"
    CATEGORICAL = "categorical"
    IGNORABLE = "ignorable"


class Problem:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.discovery_results: Any = None
        self.dataset: Any = None
        self.description: Any = None
        self.ground_truth: Any = None
        self.knowledge: Any = None
        self.estimation_results: Any = None
        self.refutation_results: Any = None


class RefutationResult:
    def __init__(
        self,
        treatment="origin",
        estimated_effect=1.096536774783349,
        p_value=0.84,
        new_effect=1.0772796171531642,
        model="SubsetRemoval",
        runtime=12.050660702007008,
        passed=True,
    ):
        self.treatment = treatment
        self.estimated_effect = estimated_effect
        self.p_value = p_value
        self.new_effect = new_effect
        self.model = model
        self.runtime = runtime
        self.passed = passed


class IdentifiedEstimand:
    def __init__(self, estimand=0.12):
        self.estimand = estimand


class CausalEstimate:
    def __init__(self, estimate=0.90):
        self.estimate = estimate


class EstimationResult:
    def __init__(
        self,
        model="BES",
        treatment="displacement",
        estimand=IdentifiedEstimand(),
        estimate=CausalEstimate(),
        control_value=0,
        treatment_value=1,
        p_value=None,
    ):
        self.model = model
        self.treatment = treatment
        self.estimand = estimand
        self.estimate = estimate
        self.control_value = control_value
        self.treatment_value = treatment_value
        self.p_value = p_value


class DiscoveryResult:
    def __init__(
        self,
        output_graph="<networkx.classes.digraph.DiGraph object at 0x7fffada58640>",
        model="BES",
        auc_pr=None,
        shd=None,
        sid=None,
        runtime=7.735817548993509,
        priority_score=0.3826530612244898,
        knowledge_integrity_score=0.875,
        forbidden_edges_violation_rate=0.125,
        required_edges_compliance_rate=1.0,
    ):
        self.output_graph = output_graph
        self.model = model
        self.auc_pr = auc_pr
        self.shd = shd
        self.sid = sid
        self.runtime = runtime
        self.priority_score = priority_score
        self.knowledge_integrity_score = knowledge_integrity_score
        self.forbidden_edges_violation_rate = forbidden_edges_violation_rate
        self.required_edges_compliance_rate = required_edges_compliance_rate


def Dataset(*args, **kwargs):
    return "dataset"


def handle_missing_data(*args, **kwargs):
    return "handle_missing_data"


def FeatureTypeMap(*args, **kwargs):
    return "feature_type_map"


def estimate_feature_importances(*args, **kwargs):
    return "dataset"


# Causal Discovery
# # Fetch applyable models
def applyable_models(*args, **kwargs):
    return ["PC", "GS", "CCDR", "IAMB", "SAM", "BES", "GRASP", "CGNN"]


# # Run discovery from these models
def discover_with_all_models(problem: Problem, *args, **kwargs):
    if problem is None:
        return None
    problem.discovery_results = {
        "PC": DiscoveryResult(
            output_graph="<networkx.classes.digraph.DiGraph object at 0x7fffada58640>",
            model="PC",
            auc_pr=None,
            shd=None,
            sid=None,
            runtime=7.735817548993509,
            priority_score=0.3826530612244898,
            knowledge_integrity_score=0.875,
            forbidden_edges_violation_rate=0.125,
            required_edges_compliance_rate=1.0,
        ),
        "GS": DiscoveryResult(
            "output_graph=<networkx.classes.digraph.DiGraph object at 0x7fffada583d0>",
            model="GS",
            auc_pr=None,
            shd=None,
            sid=None,
            runtime=1.8262713269941742,
            priority_score=0.537109375,
            knowledge_integrity_score=0.7916666666666666,
            forbidden_edges_violation_rate=0.20833333333333334,
            required_edges_compliance_rate=1.0,
        ),
        "CCDR": DiscoveryResult(
            output_graph="<networkx.classes.digraph.DiGraph object at 0x7fffada58580>",
            model="CCDR",
            auc_pr=None,
            shd=None,
            sid=None,
            runtime=2.9041824890009593,
            priority_score=0.2678571428571429,
            knowledge_integrity_score=0.5833333333333333,
            forbidden_edges_violation_rate=0.4166666666666667,
            required_edges_compliance_rate=1.0,
        ),
        "IAMB": None,
        "SAM": None,
        "BES": DiscoveryResult(
            output_graph="<networkx.classes.digraph.DiGraph object at 0x7fffada58070>",
            model="BES",
            auc_pr=None,
            shd=None,
            sid=None,
            runtime=0.5914712649973808,
            priority_score=0.8928571428571427,
            knowledge_integrity_score=0.5833333333333333,
            forbidden_edges_violation_rate=0.4166666666666667,
            required_edges_compliance_rate=1.0,
        ),
        "GRASP": None,
        "CGNN": None,
    }

    return problem


def discover_with_model(problem: Problem, *args, **kwargs):
    problem.discovery_results = DiscoveryResult()
    return problem


# Estimating
def estimate_all_effects(problem: Problem, *args, **kwargs):
    if problem.discovery_results is None:
        return None
    problem.estimation_results = {
        "BES": [
            EstimationResult(
                model="BES",
                treatment="displacement",
                estimand="<dowhy.causal_identifier.identified_estimand.IdentifiedEstimand object at 0x7fff13756e50>",
                estimate="<dowhy.causal_estimator.CausalEstimate object at 0x7fff1376ec10>",
                control_value=0,
                treatment_value=1,
                p_value=1.66064183e-90,
            ),
            EstimationResult(
                model="BES",
                treatment="cylinders",
                estimand="<dowhy.causal_identifier.identified_estimand.IdentifiedEstimand object at 0x7fff1371b760>",
                estimate="<dowhy.causal_estimator.CausalEstimate object at 0x7fff1371bdc0>",
                control_value=0,
                treatment_value=1,
                p_value=0.19430199,
            ),
            EstimationResult(
                model="BES",
                treatment="weight",
                estimand="<dowhy.causal_identifier.identified_estimand.IdentifiedEstimand object at 0x7fff13727640>",
                estimate="<dowhy.causal_estimator.CausalEstimate object at 0x7fff13727970>",
                control_value=0,
                treatment_value=1,
                p_value=8.36162444e-107,
            ),
            EstimationResult(
                model="BES",
                treatment="modelyear",
                estimand="<dowhy.causal_identifier.identified_estimand.IdentifiedEstimand object at 0x7fff1372e1f0>",
                estimate="<dowhy.causal_estimator.CausalEstimate object at 0x7fff1372e550>",
                control_value=0,
                treatment_value=1,
                p_value=6.8892806e-28,
            ),
            EstimationResult(
                model="BES",
                treatment="horsepower",
                estimand="<dowhy.causal_identifier.identified_estimand.IdentifiedEstimand object at 0x7fff1372ed90>",
                estimate="<dowhy.causal_estimator.CausalEstimate object at 0x7fff13737130>",
                control_value=0,
                treatment_value=1,
                p_value=0.0108623,
            ),
            EstimationResult(
                model="BES",
                treatment="acceleration",
                estimand="<dowhy.causal_identifier.identified_estimand.IdentifiedEstimand object at 0x7fff13737970>",
                estimate="<dowhy.causal_estimator.CausalEstimate object at 0x7fff13737e20>",
                control_value=0,
                treatment_value=1,
                p_value=7.62488697e-06,
            ),
            EstimationResult(
                model="BES",
                treatment="origin",
                estimand="<dowhy.causal_identifier.identified_estimand.IdentifiedEstimand object at 0x7fff136c06a0>",
                estimate="<dowhy.causal_estimator.CausalEstimate object at 0x7fff136c0700>",
                control_value=0,
                treatment_value=1,
                p_value=None,
            ),
        ],
        "GS": [
            EstimationResult(
                model="GS",
                treatment="displacement",
                estimand="<dowhy.causal_identifier.identified_estimand.IdentifiedEstimand object at 0x7fff137b1e20>",
                estimate="<dowhy.causal_estimator.CausalEstimate object at 0x7fff137492e0>",
                control_value=0,
                treatment_value=1,
                p_value=6.63414735e-10,
            ),
            EstimationResult(
                model="GS",
                treatment="cylinders",
                estimand="<dowhy.causal_identifier.identified_estimand.IdentifiedEstimand object at 0x7fff1376adf0>",
                estimate="<dowhy.causal_estimator.CausalEstimate object at 0x7fff1376ae50>",
                control_value=0,
                treatment_value=1,
                p_value=None,
            ),
            EstimationResult(
                model="GS",
                treatment="weight",
                estimand="<dowhy.causal_identifier.identified_estimand.IdentifiedEstimand object at 0x7fff1376aeb0>",
                estimate="<dowhy.causal_estimator.CausalEstimate object at 0x7fff1376e9a0>",
                control_value=0,
                treatment_value=1,
                p_value=2.55803087e-50,
            ),
            EstimationResult(
                model="GS",
                treatment="modelyear",
                estimand="<dowhy.causal_identifier.identified_estimand.IdentifiedEstimand object at 0x7fff1377b400>",
                estimate="<dowhy.causal_estimator.CausalEstimate object at 0x7fff1377be80>",
                control_value=0,
                treatment_value=1,
                p_value=2.33563279e-50,
            ),
            EstimationResult(
                model="GS",
                treatment="horsepower",
                estimand="<dowhy.causal_identifier.identified_estimand.IdentifiedEstimand object at 0x7fff13704700>",
                estimate="<dowhy.causal_estimator.CausalEstimate object at 0x7fff13704bb0>",
                control_value=0,
                treatment_value=1,
                p_value=2.85913426e-19,
            ),
            EstimationResult(
                model="GS",
                treatment="acceleration",
                estimand="<dowhy.causal_identifier.identified_estimand.IdentifiedEstimand object at 0x7fff1370b4f0>",
                estimate="<dowhy.causal_estimator.CausalEstimate object at 0x7fff1370b8b0>",
                control_value=0,
                treatment_value=1,
                p_value=2.28040429e-34,
            ),
            EstimationResult(
                model="GS",
                treatment="origin",
                estimand="<dowhy.causal_identifier.identified_estimand.IdentifiedEstimand object at 0x7fff137144c0>",
                estimate="<dowhy.causal_estimator.CausalEstimate object at 0x7fff13714f70>",
                control_value=0,
                treatment_value=1,
                p_value=4.6320937e-08,
            ),
        ],
        "PC": [
            EstimationResult(
                model="PC",
                treatment="displacement",
                estimand="<dowhy.causal_identifier.identified_estimand.IdentifiedEstimand object at 0x7fff137ab790>",
                estimate="<dowhy.causal_estimator.CausalEstimate object at 0x7fff137b1e50>",
                control_value=0,
                treatment_value=1,
                p_value=1.5168687e-17,
            ),
            EstimationResult(
                model="PC",
                treatment="cylinders",
                estimand="<dowhy.causal_identifier.identified_estimand.IdentifiedEstimand object at 0x7fff13740520>",
                estimate="<dowhy.causal_estimator.CausalEstimate object at 0x7fff13740580>",
                control_value=0,
                treatment_value=1,
                p_value=None,
            ),
            EstimationResult(
                model="PC",
                treatment="weight",
                estimand="<dowhy.causal_identifier.identified_estimand.IdentifiedEstimand object at 0x7fff137405e0>",
                estimate="<dowhy.causal_estimator.CausalEstimate object at 0x7fff13740f10>",
                control_value=0,
                treatment_value=1,
                p_value=2.55803087e-50,
            ),
            EstimationResult(
                model="PC",
                treatment="modelyear",
                estimand="<dowhy.causal_identifier.identified_estimand.IdentifiedEstimand object at 0x7fff13749e20>",
                estimate="<dowhy.causal_estimator.CausalEstimate object at 0x7fff137565b0>",
                control_value=0,
                treatment_value=1,
                p_value=2.90270922e-56,
            ),
            EstimationResult(
                model="PC",
                treatment="horsepower",
                estimand="<dowhy.causal_identifier.identified_estimand.IdentifiedEstimand object at 0x7fff1375b280>",
                estimate="<dowhy.causal_estimator.CausalEstimate object at 0x7fff1375bdf0>",
                control_value=0,
                treatment_value=1,
                p_value=2.85913426e-19,
            ),
            EstimationResult(
                model="PC",
                treatment="acceleration",
                estimand="<dowhy.causal_identifier.identified_estimand.IdentifiedEstimand object at 0x7fff13762ac0>",
                estimate="<dowhy.causal_estimator.CausalEstimate object at 0x7fff13762b20>",
                control_value=0,
                treatment_value=1,
                p_value=None,
            ),
            EstimationResult(
                model="PC",
                treatment="origin",
                estimand="<dowhy.causal_identifier.identified_estimand.IdentifiedEstimand object at 0x7fff13762b80>",
                estimate="<dowhy.causal_estimator.CausalEstimate object at 0x7fff1376a970>",
                control_value=0,
                treatment_value=1,
                p_value=4.6320937e-08,
            ),
        ],
        "CCDR": [
            EstimationResult(
                model="CCDR",
                treatment="displacement",
                estimand="<dowhy.causal_identifier.identified_estimand.IdentifiedEstimand object at 0x7fff137b9be0>",
                estimate="<dowhy.causal_estimator.CausalEstimate object at 0x7fff13740f70>",
                control_value=0,
                treatment_value=1,
                p_value=1.66064183e-90,
            ),
            EstimationResult(
                model="CCDR",
                treatment="cylinders",
                estimand="<dowhy.causal_identifier.identified_estimand.IdentifiedEstimand object at 0x7fff13704070>",
                estimate="<dowhy.causal_estimator.CausalEstimate object at 0x7fff137040d0>",
                control_value=0,
                treatment_value=1,
                p_value=None,
            ),
            EstimationResult(
                model="CCDR",
                treatment="weight",
                estimand="<dowhy.causal_identifier.identified_estimand.IdentifiedEstimand object at 0x7fff13704130>",
                estimate="<dowhy.causal_estimator.CausalEstimate object at 0x7fff13704190>",
                control_value=0,
                treatment_value=1,
                p_value=None,
            ),
            EstimationResult(
                model="CCDR",
                treatment="modelyear",
                estimand="<dowhy.causal_identifier.identified_estimand.IdentifiedEstimand object at 0x7fff137041f0>",
                estimate="<dowhy.causal_estimator.CausalEstimate object at 0x7fff13704250>",
                control_value=0,
                treatment_value=1,
                p_value=None,
            ),
            EstimationResult(
                model="CCDR",
                treatment="horsepower",
                estimand="<dowhy.causal_identifier.identified_estimand.IdentifiedEstimand object at 0x7fff137042b0>",
                estimate="<dowhy.causal_estimator.CausalEstimate object at 0x7fff13704310>",
                control_value=0,
                treatment_value=1,
                p_value=None,
            ),
            EstimationResult(
                model="CCDR",
                treatment="acceleration",
                estimand="<dowhy.causal_identifier.identified_estimand.IdentifiedEstimand object at 0x7fff13704370>",
                estimate="<dowhy.causal_estimator.CausalEstimate object at 0x7fff137043d0>",
                control_value=0,
                treatment_value=1,
                p_value=None,
            ),
            EstimationResult(
                model="CCDR",
                treatment="origin",
                estimand="<dowhy.causal_identifier.identified_estimand.IdentifiedEstimand object at 0x7fff13704430>",
                estimate="<dowhy.causal_estimator.CausalEstimate object at 0x7fff1370b040>",
                control_value=0,
                treatment_value=1,
                p_value=0.00284554,
            ),
        ],
    }
    return problem


def estimate_model_effects(problem: Problem, *args, **kwargs):
    problem.estimation_results = [
        EstimationResult(),
        EstimationResult(),
        EstimationResult(),
    ]
    return problem


# Refuting
def refute_all_results(problem: Problem, *args, **kwargs):
    if problem.estimation_results is None:
        return None
    problem.refutation_results = {
        "BES": [
            RefutationResult(
                treatment="modelyear",
                estimated_effect=0.6962122587522863,
                p_value=0.98,
                new_effect=-0.0006480053511358541,
                model="PlaceboPermute",
                runtime=13.309877563006012,
                passed=True,
            ),
            RefutationResult(
                treatment="modelyear",
                estimated_effect=0.6962122587522863,
                p_value=0.94,
                new_effect=0.6956993074502753,
                model="RandomCommonCause",
                runtime=12.784483821000322,
                passed=True,
            ),
            RefutationResult(
                treatment="modelyear",
                estimated_effect=0.6962122587522863,
                p_value=0.96,
                new_effect=0.6953970199677232,
                model="SubsetRemoval",
                runtime=19.351473714996246,
                passed=True,
            ),
            RefutationResult(
                treatment="weight",
                estimated_effect=-0.006632075291840067,
                p_value=0.8999999999999999,
                new_effect=2.5692487027768606e-05,
                model="PlaceboPermute",
                runtime=13.319387529001688,
                passed=True,
            ),
            RefutationResult(
                treatment="weight",
                estimated_effect=-0.006632075291840067,
                p_value=0.88,
                new_effect=-0.006632310862542212,
                model="RandomCommonCause",
                runtime=11.83800112499739,
                passed=True,
            ),
            RefutationResult(
                treatment="weight",
                estimated_effect=-0.006632075291840067,
                p_value=0.94,
                new_effect=-0.006633002462394657,
                model="SubsetRemoval",
                runtime=16.367158948996803,
                passed=True,
            ),
            RefutationResult(
                treatment="horsepower",
                estimated_effect=-0.03078627824347535,
                p_value=0.92,
                new_effect=-0.0003014391016042595,
                model="PlaceboPermute",
                runtime=13.229063733000658,
                passed=True,
            ),
            RefutationResult(
                treatment="horsepower",
                estimated_effect=-0.03078627824347535,
                p_value=0.94,
                new_effect=-0.030764262667205174,
                model="RandomCommonCause",
                runtime=10.74040625699854,
                passed=True,
            ),
            RefutationResult(
                treatment="horsepower",
                estimated_effect=-0.03078627824347535,
                p_value=0.8999999999999999,
                new_effect=-0.03080678638727907,
                model="SubsetRemoval",
                runtime=17.586922645990853,
                passed=True,
            ),
            RefutationResult(
                treatment="displacement",
                estimated_effect=-0.06005142781220485,
                p_value=0.8999999999999999,
                new_effect=0.0005067503665192419,
                model="PlaceboPermute",
                runtime=14.859410688994103,
                passed=True,
            ),
            RefutationResult(
                treatment="displacement",
                estimated_effect=-0.06005142781220485,
                p_value=0.96,
                new_effect=-0.0600508502023915,
                model="RandomCommonCause",
                runtime=29.70808085500903,
                passed=True,
            ),
            RefutationResult(
                treatment="displacement",
                estimated_effect=-0.06005142781220485,
                p_value=0.9,
                new_effect=-0.06006614453590586,
                model="SubsetRemoval",
                runtime=41.18913261000125,
                passed=True,
            ),
            RefutationResult(
                treatment="acceleration",
                estimated_effect=-0.4581231038215492,
                p_value=0.96,
                new_effect=0.001530024720015355,
                model="PlaceboPermute",
                runtime=21.484741431006114,
                passed=True,
            ),
            RefutationResult(
                treatment="acceleration",
                estimated_effect=-0.4581231038215492,
                p_value=0.8999999999999999,
                new_effect=-0.45725209113511595,
                model="RandomCommonCause",
                runtime=57.73011397400114,
                passed=True,
            ),
            RefutationResult(
                treatment="acceleration",
                estimated_effect=-0.4581231038215492,
                p_value=0.94,
                new_effect=-0.4551714780773629,
                model="SubsetRemoval",
                runtime=49.276850611000555,
                passed=True,
            ),
            RefutationResult(
                treatment="cylinders",
                estimated_effect=-0.5763477185811396,
                p_value=0.88,
                new_effect=-0.004702077685628296,
                model="PlaceboPermute",
                runtime=20.581190242999583,
                passed=True,
            ),
            RefutationResult(
                treatment="cylinders",
                estimated_effect=-0.5763477185811396,
                p_value=0.9,
                new_effect=-0.5739231912594929,
                model="RandomCommonCause",
                runtime=54.64347519801231,
                passed=True,
            ),
            RefutationResult(
                treatment="cylinders",
                estimated_effect=-0.5763477185811396,
                p_value=0.8999999999999999,
                new_effect=-0.5516298164413247,
                model="SubsetRemoval",
                runtime=46.069152210009634,
                passed=True,
            ),
        ],
        "GS": [
            RefutationResult(
                treatment="modelyear",
                estimated_effect=0.7243023052489228,
                p_value=0.9,
                new_effect=-0.0019545501557946742,
                model="PlaceboPermute",
                runtime=12.256437383999582,
                passed=True,
            ),
            RefutationResult(
                treatment="modelyear",
                estimated_effect=0.7243023052489228,
                p_value=0.94,
                new_effect=0.7240506211873137,
                model="RandomCommonCause",
                runtime=12.631640224994044,
                passed=True,
            ),
            RefutationResult(
                treatment="modelyear",
                estimated_effect=0.7243023052489228,
                p_value=0.92,
                new_effect=0.7235866786663442,
                model="SubsetRemoval",
                runtime=18.02998996700626,
                passed=True,
            ),
            RefutationResult(
                treatment="origin",
                estimated_effect=0.4228250695274802,
                p_value=0.98,
                new_effect=-0.0034992044587161784,
                model="PlaceboPermute",
                runtime=11.338135842001066,
                passed=True,
            ),
            RefutationResult(
                treatment="origin",
                estimated_effect=0.4228250695274802,
                p_value=0.94,
                new_effect=0.42209356632847056,
                model="RandomCommonCause",
                runtime=14.749319105001632,
                passed=True,
            ),
            RefutationResult(
                treatment="origin",
                estimated_effect=0.4228250695274802,
                p_value=0.94,
                new_effect=0.4101590980841081,
                model="SubsetRemoval",
                runtime=19.195237900989014,
                passed=True,
            ),
            RefutationResult(
                treatment="weight",
                estimated_effect=-0.005817402342373157,
                p_value=1.0,
                new_effect=4.538343660271948e-06,
                model="PlaceboPermute",
                runtime=14.757083024000167,
                passed=True,
            ),
            RefutationResult(
                treatment="weight",
                estimated_effect=-0.005817402342373157,
                p_value=0.92,
                new_effect=-0.005818045634699871,
                model="RandomCommonCause",
                runtime=14.780345029997989,
                passed=True,
            ),
            RefutationResult(
                treatment="weight",
                estimated_effect=-0.005817402342373157,
                p_value=0.94,
                new_effect=-0.005823188333204783,
                model="SubsetRemoval",
                runtime=20.948813494003844,
                passed=True,
            ),
            RefutationResult(
                treatment="displacement",
                estimated_effect=-0.026678898322529676,
                p_value=0.94,
                new_effect=4.593756790271186e-05,
                model="PlaceboPermute",
                runtime=14.842974037004751,
                passed=True,
            ),
            RefutationResult(
                treatment="displacement",
                estimated_effect=-0.026678898322529676,
                p_value=0.98,
                new_effect=-0.026697373562696212,
                model="RandomCommonCause",
                runtime=14.736193341988837,
                passed=True,
            ),
            RefutationResult(
                treatment="displacement",
                estimated_effect=-0.026678898322529676,
                p_value=0.96,
                new_effect=-0.026798798354993957,
                model="SubsetRemoval",
                runtime=22.046915643993998,
                passed=True,
            ),
            RefutationResult(
                treatment="horsepower",
                estimated_effect=-0.10513959150160446,
                p_value=0.9,
                new_effect=-0.00031513838037227514,
                model="PlaceboPermute",
                runtime=19.20667349100404,
                passed=True,
            ),
            RefutationResult(
                treatment="horsepower",
                estimated_effect=-0.10513959150160446,
                p_value=0.9199999999999999,
                new_effect=-0.10513158727598708,
                model="RandomCommonCause",
                runtime=68.22706869601097,
                passed=True,
            ),
            RefutationResult(
                treatment="horsepower",
                estimated_effect=-0.10513959150160446,
                p_value=0.84,
                new_effect=-0.10591083955172045,
                model="SubsetRemoval",
                runtime=48.56385316500382,
                passed=True,
            ),
            RefutationResult(
                treatment="acceleration",
                estimated_effect=-0.43106903117922357,
                p_value=0.94,
                new_effect=0.0003080257194896419,
                model="PlaceboPermute",
                runtime=33.544154821996926,
                passed=True,
            ),
            RefutationResult(
                treatment="acceleration",
                estimated_effect=-0.43106903117922357,
                p_value=0.8,
                new_effect=-0.4302554122255687,
                model="RandomCommonCause",
                runtime=61.9705027960008,
                passed=True,
            ),
            RefutationResult(
                treatment="acceleration",
                estimated_effect=-0.43106903117922357,
                p_value=0.8999999999999999,
                new_effect=-0.4281132968254333,
                model="SubsetRemoval",
                runtime=56.45508396500372,
                passed=True,
            ),
        ],
        "PC": [
            RefutationResult(
                treatment="modelyear",
                estimated_effect=0.7199204929632685,
                p_value=0.9,
                new_effect=-0.0018695590755184455,
                model="PlaceboPermute",
                runtime=12.389438775004237,
                passed=True,
            ),
            RefutationResult(
                treatment="modelyear",
                estimated_effect=0.7199204929632685,
                p_value=0.94,
                new_effect=0.7197147970192448,
                model="RandomCommonCause",
                runtime=11.397438417989179,
                passed=True,
            ),
            RefutationResult(
                treatment="modelyear",
                estimated_effect=0.7199204929632685,
                p_value=0.92,
                new_effect=0.7188985053114467,
                model="SubsetRemoval",
                runtime=18.657960077005555,
                passed=True,
            ),
            RefutationResult(
                treatment="origin",
                estimated_effect=0.4228250695274802,
                p_value=0.98,
                new_effect=-0.0034992044587161784,
                model="PlaceboPermute",
                runtime=11.347903885005508,
                passed=True,
            ),
            RefutationResult(
                treatment="origin",
                estimated_effect=0.4228250695274802,
                p_value=0.94,
                new_effect=0.42209356632847056,
                model="RandomCommonCause",
                runtime=12.926975466994918,
                passed=True,
            ),
            RefutationResult(
                treatment="origin",
                estimated_effect=0.4228250695274802,
                p_value=0.94,
                new_effect=0.4101590980841081,
                model="SubsetRemoval",
                runtime=13.648918628998217,
                passed=True,
            ),
            RefutationResult(
                treatment="weight",
                estimated_effect=-0.005817402342373157,
                p_value=1.0,
                new_effect=4.538343660271948e-06,
                model="PlaceboPermute",
                runtime=14.823989980999613,
                passed=True,
            ),
            RefutationResult(
                treatment="weight",
                estimated_effect=-0.005817402342373157,
                p_value=0.92,
                new_effect=-0.005818045634699871,
                model="RandomCommonCause",
                runtime=16.102807176008355,
                passed=True,
            ),
            RefutationResult(
                treatment="weight",
                estimated_effect=-0.005817402342373157,
                p_value=0.94,
                new_effect=-0.005823188333204783,
                model="SubsetRemoval",
                runtime=21.556404953997117,
                passed=True,
            ),
            RefutationResult(
                treatment="displacement",
                estimated_effect=-0.04508724237715711,
                p_value=0.98,
                new_effect=0.00012156778617615771,
                model="PlaceboPermute",
                runtime=16.731118946001516,
                passed=True,
            ),
            RefutationResult(
                treatment="displacement",
                estimated_effect=-0.04508724237715711,
                p_value=0.9199999999999999,
                new_effect=-0.045092032806919986,
                model="RandomCommonCause",
                runtime=17.34355659400171,
                passed=True,
            ),
            RefutationResult(
                treatment="displacement",
                estimated_effect=-0.04508724237715711,
                p_value=0.82,
                new_effect=-0.045169579491836274,
                model="SubsetRemoval",
                runtime=23.132196064994787,
                passed=True,
            ),
            RefutationResult(
                treatment="horsepower",
                estimated_effect=-0.10513959150160446,
                p_value=0.9,
                new_effect=-0.00031513838037227514,
                model="PlaceboPermute",
                runtime=16.7371939420118,
                passed=True,
            ),
            RefutationResult(
                treatment="horsepower",
                estimated_effect=-0.10513959150160446,
                p_value=0.9199999999999999,
                new_effect=-0.10513158727598708,
                model="RandomCommonCause",
                runtime=62.690559585011215,
                passed=True,
            ),
            RefutationResult(
                treatment="horsepower",
                estimated_effect=-0.10513959150160446,
                p_value=0.84,
                new_effect=-0.10591083955172045,
                model="SubsetRemoval",
                runtime=38.04266793899296,
                passed=True,
            ),
        ],
        "CCDR": [
            RefutationResult(
                treatment="origin",
                estimated_effect=1.096536774783349,
                p_value=0.94,
                new_effect=0.01776416640637173,
                model="PlaceboPermute",
                runtime=12.581017632008297,
                passed=True,
            ),
            RefutationResult(
                treatment="origin",
                estimated_effect=1.096536774783349,
                p_value=0.94,
                new_effect=1.0970506381351885,
                model="RandomCommonCause",
                runtime=12.665284888003953,
                passed=True,
            ),
            RefutationResult(
                treatment="origin",
                estimated_effect=1.096536774783349,
                p_value=0.84,
                new_effect=1.0772796171531642,
                model="SubsetRemoval",
                runtime=12.050660702007008,
                passed=True,
            ),
            RefutationResult(
                treatment="displacement",
                estimated_effect=-0.06005142781220485,
                p_value=0.8999999999999999,
                new_effect=0.0005067503665192419,
                model="PlaceboPermute",
                runtime=14.012264514007256,
                passed=True,
            ),
            RefutationResult(
                treatment="displacement",
                estimated_effect=-0.06005142781220485,
                p_value=0.96,
                new_effect=-0.0600508502023915,
                model="RandomCommonCause",
                runtime=34.258695978001924,
                passed=True,
            ),
            RefutationResult(
                treatment="displacement",
                estimated_effect=-0.06005142781220485,
                p_value=0.9,
                new_effect=-0.06006614453590586,
                model="SubsetRemoval",
                runtime=42.13767303900386,
                passed=True,
            ),
        ],
    }
    return problem


def refute_estimation(problem: Problem, *args, **kwargs):
    problem.refutation_results = RefutationResult()
    return problem


# Visualizing
def generate_result_graph(*args, **kwargs):
    return (
        'digraph G {\nfontname="Helvetica,Arial,sans-serif";\nnode[style="filled", fontsize=20, penwidth=2.5, fixedsize=true, fontcolor="black", fillcolor="gray", color="black", shape="circle"];\nedge[penwidth=2, minlen=2];\nsplines="polyline";\n   "displacement"[width=1, height=1, label="displacement\n-0.05", fillcolor="lightpink"];\n   "cylinders"[width=1, height=1, label="cylinders\n0.00", fillcolor="gray;0.25:lightgray;0.25:gray;0.25:lightgray;0.25", color="lightgray", style="wedged", shape="doublecircle"];\n   "weight"[width=1, height=1, label="weight\n-0.01", fillcolor="lightpink"];\n   "modelyear"[width=1, height=1, label="modelyear\n0.72", fillcolor="#4CAF50", fontcolor="white"];\n   "horsepower"[width=1, height=1, label="horsepower\n-0.11", fillcolor="lightpink"];\n   "acceleration"[width=1, height=1, label="acceleration\n0.00", fillcolor="gray;0.25:lightgray;0.25:gray;0.25:lightgray;0.25", color="lightgray", style="wedged", shape="doublecircle"];\n   "origin"[width=1, height=1, label="origin\n0.42", fillcolor="#4CAF50", fontcolor="white"];\n   "mpg"[width=1, height=1, label="mpg", fillcolor="magenta", color="purple", shape="hexagon", fontcolor="white"];\n   "displacement" -> "cylinders"[color=red];\n   "displacement" -> "weight"[color=red];\n   "weight" -> "mpg"[color=black];\n   "modelyear" -> "mpg"[color=black];\n   "horsepower" -> "displacement"[color=red];\n   "horsepower" -> "acceleration"[color=black];\n   "origin" -> "displacement"[color=black];\n   "origin" -> "mpg"[color=black];\n}',
    )


def generate_all_results(problem):
    if problem.discovery_results is None:
        return None
    else:
        return {
            "PC": 'digraph G {\nfontname="Helvetica,Arial,sans-serif";\nnode[style="filled", fontsize=20, penwidth=2.5, fixedsize=true, fontcolor="black", fillcolor="gray", color="black", shape="circle"];\nedge[penwidth=2, minlen=2];\nsplines="polyline";\n   "displacement"[width=1, height=1, label="displacement\n-0.05", fillcolor="lightpink"];\n   "cylinders"[width=1, height=1, label="cylinders\n0.00", fillcolor="gray;0.25:lightgray;0.25:gray;0.25:lightgray;0.25", color="lightgray", style="wedged", shape="doublecircle"];\n   "weight"[width=1, height=1, label="weight\n-0.01", fillcolor="lightpink"];\n   "modelyear"[width=1, height=1, label="modelyear\n0.72", fillcolor="#4CAF50", fontcolor="white"];\n   "horsepower"[width=1, height=1, label="horsepower\n-0.11", fillcolor="lightpink"];\n   "acceleration"[width=1, height=1, label="acceleration\n0.00", fillcolor="gray;0.25:lightgray;0.25:gray;0.25:lightgray;0.25", color="lightgray", style="wedged", shape="doublecircle"];\n   "origin"[width=1, height=1, label="origin\n0.42", fillcolor="#4CAF50", fontcolor="white"];\n   "mpg"[width=1, height=1, label="mpg", fillcolor="magenta", color="purple", shape="hexagon", fontcolor="white"];\n   "displacement" -> "cylinders"[color=red];\n   "displacement" -> "weight"[color=red];\n   "weight" -> "mpg"[color=black];\n   "modelyear" -> "mpg"[color=black];\n   "horsepower" -> "displacement"[color=red];\n   "horsepower" -> "acceleration"[color=black];\n   "origin" -> "displacement"[color=black];\n   "origin" -> "mpg"[color=black];\n}',
            "GS": 'digraph G {\nfontname="Helvetica,Arial,sans-serif";\nnode[style="filled", fontsize=20, penwidth=2.5, fixedsize=true, fontcolor="black", fillcolor="gray", color="black", shape="circle"];\nedge[penwidth=2, minlen=2];\nsplines="polyline";\n   "displacement"[width=1, height=1, label="displacement\n-0.03", fillcolor="lightpink"];\n   "cylinders"[width=1, height=1, label="cylinders\n0.00", fillcolor="gray;0.25:lightgray;0.25:gray;0.25:lightgray;0.25", color="lightgray", style="wedged", shape="doublecircle"];\n   "weight"[width=1, height=1, label="weight\n-0.01", fillcolor="lightpink"];\n   "modelyear"[width=1, height=1, label="modelyear\n0.72", fillcolor="#4CAF50", fontcolor="white"];\n   "horsepower"[width=1, height=1, label="horsepower\n-0.11", fillcolor="lightpink"];\n   "acceleration"[width=1, height=1, label="acceleration\n-0.43", fillcolor="lightpink"];\n   "origin"[width=1, height=1, label="origin\n0.42", fillcolor="#4CAF50", fontcolor="white"];\n   "mpg"[width=1, height=1, label="mpg", fillcolor="magenta", color="purple", shape="hexagon", fontcolor="white"];\n   "displacement" -> "cylinders"[color=red];\n   "displacement" -> "weight"[color=red];\n   "displacement" -> "acceleration"[color=black];\n   "weight" -> "mpg"[color=black];\n   "modelyear" -> "mpg"[color=black];\n   "horsepower" -> "displacement"[color=red];\n   "horsepower" -> "weight"[color=red];\n   "horsepower" -> "acceleration"[color=black];\n   "acceleration" -> "weight"[color=red];\n   "origin" -> "displacement"[color=black];\n   "origin" -> "mpg"[color=black];\n}',
            "CCDR": 'digraph G {\nfontname="Helvetica,Arial,sans-serif";\nnode[style="filled", fontsize=20, penwidth=2.5, fixedsize=true, fontcolor="black", fillcolor="gray", color="black", shape="circle"];\nedge[penwidth=2, minlen=2];\nsplines="polyline";\n   "displacement"[width=1, height=1, label="displacement\n-0.06", fillcolor="lightpink"];\n   "cylinders"[width=1, height=1, label="cylinders\n0.00", fillcolor="gray;0.25:lightgray;0.25:gray;0.25:lightgray;0.25", color="lightgray", style="wedged", shape="doublecircle"];\n   "weight"[width=1, height=1, label="weight\n0.00", fillcolor="gray;0.25:lightgray;0.25:gray;0.25:lightgray;0.25", color="lightgray", style="wedged", shape="doublecircle"];\n   "modelyear"[width=1, height=1, label="modelyear\n0.00", fillcolor="gray;0.25:lightgray;0.25:gray;0.25:lightgray;0.25", color="lightgray", style="wedged", shape="doublecircle"];\n   "horsepower"[width=1, height=1, label="horsepower\n0.00", fillcolor="gray;0.25:lightgray;0.25:gray;0.25:lightgray;0.25", color="lightgray", style="wedged", shape="doublecircle"];\n   "acceleration"[width=1, height=1, label="acceleration\n0.00", fillcolor="gray;0.25:lightgray;0.25:gray;0.25:lightgray;0.25", color="lightgray", style="wedged", shape="doublecircle"];\n   "origin"[width=1, height=1, label="origin\n1.10", fillcolor="#4CAF50", fontcolor="white"];\n   "mpg"[width=1, height=1, label="mpg", fillcolor="magenta", color="purple", shape="hexagon", fontcolor="white"];\n   "displacement" -> "cylinders"[color=red];\n   "displacement" -> "weight"[color=red];\n   "displacement" -> "modelyear"[color=red];\n   "displacement" -> "horsepower"[color=black];\n   "displacement" -> "acceleration"[color=black];\n   "displacement" -> "origin"[color=red];\n   "displacement" -> "mpg"[color=black];\n   "modelyear" -> "weight"[color=black];\n   "modelyear" -> "acceleration"[color=black];\n   "horsepower" -> "weight"[color=red];\n   "horsepower" -> "acceleration"[color=black];\n   "acceleration" -> "weight"[color=red];\n   "origin" -> "cylinders"[color=black];\n   "origin" -> "modelyear"[color=black];\n   "origin" -> "horsepower"[color=black];\n   "origin" -> "mpg"[color=black];\n   "mpg" -> "cylinders"[color=red];\n   "mpg" -> "weight"[color=red];\n   "mpg" -> "modelyear"[color=red];\n   "mpg" -> "horsepower"[color=red];\n   "mpg" -> "acceleration"[color=black];\n}',
            "IAMB": None,
            "SAM": None,
            "BES": 'digraph G {\nfontname="Helvetica,Arial,sans-serif";\nnode[style="filled", fontsize=20, penwidth=2.5, fixedsize=true, fontcolor="black", fillcolor="gray", color="black", shape="circle"];\nedge[penwidth=2, minlen=2];\nsplines="polyline";\n   "displacement"[width=1, height=1, label="displacement\n-0.06", fillcolor="lightpink"];\n   "cylinders"[width=1, height=1, label="cylinders\n-0.58", fillcolor="lightpink"];\n   "weight"[width=1, height=1, label="weight\n-0.01", fillcolor="lightpink"];\n   "modelyear"[width=1, height=1, label="modelyear\n0.70", fillcolor="#4CAF50", fontcolor="white"];\n   "horsepower"[width=1, height=1, label="horsepower\n-0.03", fillcolor="lightpink"];\n   "acceleration"[width=1, height=1, label="acceleration\n-0.46", fillcolor="lightpink"];\n   "origin"[width=1, height=1, label="origin\n0.00", fillcolor="gray;0.25:lightgray;0.25:gray;0.25:lightgray;0.25", color="lightgray", style="wedged", shape="doublecircle"];\n   "mpg"[width=1, height=1, label="mpg", fillcolor="magenta", color="purple", shape="hexagon", fontcolor="white"];\n   "displacement" -> "cylinders"[color=red];\n   "displacement" -> "weight"[color=red];\n   "displacement" -> "modelyear"[color=red];\n   "displacement" -> "horsepower"[color=black];\n   "displacement" -> "origin"[color=red];\n   "cylinders" -> "modelyear"[color=red];\n   "cylinders" -> "acceleration"[color=black];\n   "cylinders" -> "origin"[color=red];\n   "weight" -> "mpg"[color=black];\n   "modelyear" -> "horsepower"[color=black];\n   "modelyear" -> "acceleration"[color=black];\n   "modelyear" -> "mpg"[color=black];\n   "horsepower" -> "weight"[color=red];\n   "horsepower" -> "acceleration"[color=black];\n   "horsepower" -> "origin"[color=red];\n   "acceleration" -> "weight"[color=red];\n   "mpg" -> "origin"[color=red];\n}',
            "GRASP": None,
            "CGNN": None,
        }


def parse_knowledge_file(*args, **kwargs):
    return "parse_knowledge_file"
