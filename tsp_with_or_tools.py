from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2


def tsp_with_or_tools(distance_matrix):
    tsp_size = len(distance_matrix)
    routing = pywrapcp.RoutingModel(tsp_size, 1, 0)
    search_parameters = pywrapcp.RoutingModel.DefaultSearchParameters()

    def distance_callback(from_node, to_node):
        return distance_matrix[from_node][to_node]

    routing.SetArcCostEvaluatorOfAllVehicles(distance_callback)
    assignment = routing.SolveWithParameters(search_parameters)

    if assignment:
        route = []
        index = routing.Start(0)
        while not routing.IsEnd(index):
            route.append(routing.IndexToNode(index))
            index = assignment.Value(routing.NextVar(index))
        route.append(routing.IndexToNode(index))
        return route


distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]


print(tsp_with_or_tools(distance_matrix))
