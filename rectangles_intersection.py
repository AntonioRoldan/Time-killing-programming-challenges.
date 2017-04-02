
from math import sqrt

x1 = 4
y1 = 6
x2 = 7
y2 = 2
heightA = 14
heightB = 3
weightA = 8
weightB = 20
rectangleA = {'x_coordinate':x1, 'y_coordinate':y1, 'height':heightA, 'weight':weightA}
rectangleB = {'x_coordinate':x2, 'y_coordinate':y2, 'height':heightB, 'weight':weightB}

def vector(x1, y1, x2, y2):
    """Calculates the main vector of a straight line given two points"""
    vector_x = x2 - x1
    vector_y = y2 - y1
    return [vector_x, vector_y]


def areaCalculation(verticesA, verticesB, coordinatesInside):
    """Calculates area based on whether one, two or none coordinates are inside the rectangle"""
    """It will check for the four different positions rectangles can adopt"""
    if(len(coordinatesInside) == 1): #Rectangles have one vertex inside one-another
        if(coordinatesInside[0] == "Top left"): #If the coordinate in rectangle A inside B is at the top left
            vector = (verticesA[0], verticesA[1], verticesB[4], verticesB[5]) #Top left inside B necessarily implies that bottom right in B is inside A
            return "Area: " + vector[0] * vector[1] #Having the vector we multiply its components to get the answer
        elif(coordinatesInside[0] == "Top right"): #If the coordinate in rectangle A inside B is at the top right
            vector = vector(verticesA[2], verticesA[3], verticesB[6], verticesB[7]) #Top right inside B necessarily implies that bottom left in B is inside A
            return "Area: " + vector[0] * vector[1] #Having the vector we multiply its components to get the answer
        elif(coordinatesInside[0] == "Bottom right"): #If the coordinate in rectangle A inside B is at the bottom right
            vector = vector(verticesA[4], verticesA[5], verticesB[0], verticesB[1]) #Bottom right inside B necessarily implies that top left in B is inside A
            return "Area: " + vector[0] * vector[1] #Having the vector we multiply its components to get the answer
        elif(coordinatesInside[0] == "Bottom left"): #If the coordinate in rectangle A inside B is at the bottom left
            vector = (verticesA[6], verticesA[7], verticesB[2], verticesB[3]) #Bottom left inside B necessarily implies that top right in B is inside A
            return "Area: " + vector[0] * vector[1] #Having the vector we multiply its components to get the answer
    elif(len(coordinatesInside) == 2): #Rectangle A has two vertices in rectangle B
        if(coordinatesInside[0] == "Top left" and coordinatesInside[1] == "Top right"): #We want to find the intersection point at the edge from position one
            x_intersection_bottom_left = verticesA[2] #The x coordinate will be equal to the top right x coordinate in rectangle A
            y_intersection_bottom_left = verticesB[5] #The y coordinate will be equal to the bottom left or bottom right y coordinate in rectangle B
            x_intersection_bottom_right = verticesA[0] #The x coordinate will be equal to the top left x coordinate in rectangle A
            y_intersection_bottom_right = verticesB[7] #The y coordinate will be equal to the bottom right or bottom left y coordinate in rectangle B
            vector = vector(x_intersection_bottom_left, y_intersection_bottom_left, x_intersection_bottom_right, y_intersection_bottom_right) #Vector of bottom left and right coordinates
            intersection_weight = sqrt(vector[0]**2 + vector[1]**2) #We find its length, equivalent to the weight of our intersection
            vector = vector(x_intersection_bottom_left, y_intersection_bottom_left, verticesA[0], verticesA[1])
            intersection_height = sqrt(vector[0]**2 + vector[1]**2)
            return intersection_height * intersection_height
        elif(coordinatesInside[0] == "Top right" and coordinatesInside[1] == "Bottom right"): #We want to find the intersection point at the edge from position two
            x_intersection_bottom_left = verticesB[0] #The x coordinate will be equal to the top left x coordinate in rectangle B
            y_intersection_bottom_left = verticesA[3] #The y coordinate will be equal to the top right y coordinate in rectangle A
            x_intersection_bottom_right = verticesB[6] #The x coordinate will be equal to the bottom left x coordinate in rectangle B
            y_intersection_bottom_right = verticesA[5] #The y coordinate will be equal to the bottom left y coordinate in rectangle B
            vector = vector(x_intersection_bottom_left, y_intersection_bottom_left, x_intersection_bottom_right, y_intersection_bottom_right) #Vector of bottom left and right coordinates
            intersection_weight = sqrt(vector[0]**2 + vector[1]**2) #We find its length, equivalent to the weight of our intersection
            vector = vector(x_intersection_bottom_left, y_intersection_bottom_left, verticesA[2], verticesA[3]) #Vector of bottom left and top left coordinates
            intersection_height = sqrt(vector[0]**2 + vector[1]**2) #We find its length equivalent to the height of our intersection
            return intersection_height * intersection_height #We return the area
        elif(coordinatesInside[0] == "Bottom right" and coordinatesInside[1] == "Bottom left"): #We want to find the intersection point at teh edge from poisition 3
            x_intersection_bottom_right = verticesA[6] #The x coordinate will be equal to the bottom left x coordinate in rectangle A
            y_intersection_bottom_right = verticesB[1] #The y coordinate will be equal to the top left y coordinate in rectangle B
            x_intersection_bottom_left = verticesA[4] #The x coordinate will be equal to the bottom right x coordinate in rectangle A
            y_intersection_bottom_left = verticesB[3] #The y coordinate will be equal to the top right y coordinate in rectangle B
            vector = vector(x_intersection_bottom_left, y_intersection_bottom_left, x_intersection_bottom_right, y_intersection_bottom_right) #Vector of bottom left and right coordinates
            intersection_weight = sqrt(vector[0]**2 + vector[1]**2) #We find its length, equivalent to the weight of our intersection
            vector = vector(x_intersection_bottom_left, y_intersection_bottom_left, verticesA[0], vertices[1]) #Vector of bottom left and top right coordinates
            intersection_height = sqrt(vector[0]**2 + vector[1]**2) #We find its length, equivalent to the height of our intersection
            return intersection_height * intersection_height #We return the area
        elif(coordinatesInside[0] == "Top left" and coordinatesInside[1] == "Bottom left"): #Order is inverted because of the order of statements in verticesInsideRectangle
            x_intersection_bottom_left = verticesB[6] #The x coordinate will be equal to the bottom left x coordinate in rectangle B
            y_intersection_bottom_left = verticesA[7] #The y coordinate will be equal to the bottom lef y coordinate in rectangle A
            x_intersection_bottom_right = verticesB[2] #The x coordinate will be equal to the top right x coordinate in rectangle B
            y_intersection_bottom_right = verticesA[1] #The y coordinate will be equal to the top left y coordinate in rectangle A
            vector = vector(x_intersection_bottom_left, y_intersection_bottom_left, x_intersection_bottom_right, y_intersection_bottom_right) #Vector of bottom left and riht coordinates
            intersection_weight = sqrt(vector[0]**2 + vector[1]**2) #We find its length, equivalent to the weight of our intersection
            vector = vector(x_intersection_bottom_left, y_intersection_bottom_left, verticesA[6], vertices[7]) #Vector of bottom left rectangle A and bottom left in rectangle B coordinates
            intersection_height = sqrt(vector[0]**2 + vector[1]**2) #We find its length equivalent to the height of our intersection
            return intersection_height * intersection_height #We return the area
        else:
            return False

def edgeMatch(coordinatesInside, verticesA, verticesB):
    """Finds possible edge intersections between rectangles"""
    coordinatesEdge = []
    if(len(coordinatesInside) > 0):
        if(verticesA[0] == verticesB[0]):
            if(verticesA[1] <= verticesB[1] and verticesA[1] >= verticesB[7]):
                coordinatesEdge.append("Top left") #Top left coordinate is touching the edge
            else:
                pass
        if(verticesA[2] == verticesB[2]):
            if(verticesA[3] < verticesB[3] and verticesA[3] > verticesB[5]): #Top right coordinate touching the edge
                coordinatesEdge.append("Top right")
            else:
                pass
        if(verticesA[4] == verticesB[4]):
            if(verticesA[5] > verticesB[5] and verticesA[5] < verticesB[3]):
                coordinatesEdge.append("Bottom right") #Bottom right coordinate touching the edge
        if(verticesA[6] == verticesB[6]):
            if(verticesA[7] > verticesB[7] and verticesA[7] < verticesB[1]):
                coordinatesEdge.append("Bottom left") #Bottom left coordinate touching the edge
            else:
                pass

        return coordinatesEdge

    else:
        return coordinatesEdge

def verticesInsideRectangle(verticesA, verticesB):
    coordinatesInside = []
    if(verticesA[0] >= verticesB[0] and verticesA[0] <= verticesB[2] and verticesA[1] >= verticesB[7] and verticesA[1] <= verticesB[3]): #Top left coordinates
        coordinatesInside.append("Top left") #Top left inside rectangle
    if(verticesA[2] >= verticesB[0] and verticesA[2] <= verticesB[2] and verticesA[3] >= verticesB[5] and verticesA[3] <= verticesB[3]): #Top right coordinates
        coordinatesInside.append("Top right") #Top right inside rectangle
    if(verticesA[4] >= verticesB[4] and verticesA[4] <= verticesB[6] and verticesA[5] >= verticesB[7] and verticesA[5] <= verticesB[1]): #Bottom right coordinates
        coordinatesInside.append("Bottom right") #Bottom right inside rectangle
    if(verticesA[6] >= verticesB[6] and verticesA[6] <= verticesB[2] and verticesA[7] >= verticesB[7] and verticesA[7] <= verticesB[1]): #Bottom left
        coordinatesInside.append("Bottom left") #Bottom left inside rectangle
    if(all(coordinatesInside)):
        return "Totally inside"
    elif( not coordinatesInside):
        return "No vertices inside one another"
    else:
        return coordinatesInside

def findVertices(rectangle):
    vertices = []
    x_top_left = rectangle.get('x_coordinate') #First we define the top left coordinates
    y_top_left = rectangle.get('y:coordinates')
    mid_point_weight = rectangle.get('weight') // 2 + rectangle.get('x_coordinate')
    mid_point_height = rectangle.get('height') // 2 + rectangle.get('y_coordinate')
    x_top_right = rectangle.get('x_coordinate') + rectangle.get('weight') #Next top right coordinates
    y_top_right = rectangle.get('y_coordinate')
    x_bottom_right = x_top_right #Next bottom right coordinates
    y_bottom_right =  y_top_right - rectangle.get('height')
    x_bottom_left = rectangle.get('x_coordinate') #Finally bottom left coordinates
    y_bottom_left = rectangle.get('y_coordinate') - rectangle.get('height')
    vertices.append(x_top_left) #We append to a list, mentally it is like drawing a rectangle clockwise and starting at the top left vertex
    vertices.append(y_top_left) #Thus location of coordinates is easily remembered
    vertices.append(x_top_right)
    vertices.append(y_top_right)
    vertices.append(x_bottom_right)
    vertices.append(y_bottom_right)
    vertices.append(x_bottom_left)
    vertices.apppend(y_bottom_left)
    return vertices


def vertexMatch(verticesA, verticesB):
    counter = 0
    contiguous = False
    matchingVertices = []
    for i in range(8):
        if verticesA[i] == verticesB[i] and contiguous:
            matchingVertices.append(verticesA.index(verticesA[i])) #Y coordinate index, will help the computer know what vertex is matching
            contiguous = False
        elif verticesA[i] == verticesB[i]:
            contiguous = True
        else:
            if(contiguous):
                contiguous = False
            continue

    if(len(matchingVertices) >= 1): #These will all be shot in sequence accumulatively
        top_left = True             #We are checking if a rectangle perfectly matches the other
    if(len(matchingVertices) >= 2):
        top_right = True
    if(len(matchingVertices) >= 3):
        bottom_right = True
    if(len(matchingVertices) == 4):
        bottom_left = True
    if(top_left and top_right and bottom_right and bottom_left):
        return "Total match"
    else:
        return [top_left, top_right, bottom_right, bottom_left]

def verticalOrHorizontal(verticesA, verticesB):
    """Checks whether the relative position between both rectanles is vertical or horizontal"""
    """If A is vertical, B is horizontal and viceversa"""
    if(verticesA[0] > verticesB[0] and verticesA[0] < verticesB[2] and verticesA[3] > verticesB[3] and verticesA[5] < verticesB[5]): #If A is vertical with respect to B
        x_intersection_bottom_left = verticesA[0]
        y_intersection_bottom_left = verticesB[1]
        x_intersection_bottom_right = verticesA[2]
        y_intersection_bottom_right = verticesB[3]
        vector = vector(x_intersection_bottom_left, y_intersection_bottom_left, x_intersection_bottom_right, y_intersection_bottom_right)
        intersection_weight = sqrt(vector[0]**2 + vector[1]**2)
        vector = vector(x_intersection_bottom_left, y_intersection_bottom_left, verticesA[0], verticesA[1])
        intersection_height = sqrt(vector[0]**2 + vector[1]**2)
        return intersection_weight * intersection_height
    elif(verticesA[0] < verticesB[0] and verticesA[0] > verticesB[6] and verticesA[7] < verticesB[7] and verticesA[5] > verticesA[5]): #If A is horizontal with respect to B
        x_intersection_bottom_left = verticesB[0]
        y_intersection_bottom_left = verticesA[1]
        x_intersection_bottom_right = verticesB[6]
        y_intersection_bottom_right = verticesA[7]
        vector = vector(x_intersection_bottom_left, y_intersection_bottom_left, x_intersection_bottom_right, y_intersection_bottom_right)
        intersection_weight = sqrt(vector[0]**2 + vector[1]**2)
        vector = vector(x_intersection_bottom_left, y_intersection_bottom_left, verticesA[0], verticesA[1])
        intersection_height = sqrt(vector[0]**2 + vector[1]**2)
        return intersection_weight * intersection_height

def isLoveWhatWeFeelin(rectangleA, rectangleB):
    """It will check for every single possiblity for two rectangles to intersect"""
    verticesA = findVertices(rectangleA) #First we find all vertices for each rectangle
    verticesB = findVertices(rectangleB)
    if(vertexMatch(VerticesA, VerticesB) == "Total match"):
        return str(rectangleA.get('height') * rectangleA.get('weight')) #If both rectangles share all of their vertices
    AinB = verticesInsideRectangle(verticesA, verticesB)
    BinA = verticesInsideRectangle(verticesB, verticesA)
    if(AinB == "Totally inside"): #If rectangle A inside rectangle B
        return "Rectangle A is inside rectangle B\nArea of intersection: " + str(rectangleA.get('height') * rectangleA.get('weight'))
    elif(BinA == "Totally inside"): #If rectangle B inside rectangle A
        return "Rectangle B is inside rectangle A\n Area of intersection : " + str(rectangleB.get('height') * rectangleB.get('weight'))
    elif(AinB == "No vertices inside one-another"): #We could use BinA too
        return str(verticalOrHorizontal(verticesA, verticesB))
    else:
        coordinatesInsideA = BinA
        coordinatesInsideB = AinB
        coordinatesEdge(coordinatesInsideB, verticesA, verticesB)
        resultA = areaCalculation(verticesA, verticesB, coordinatesInsideB) #Assuming rectangle A is inside B
        resultB = areaCalculation(verticesA, verticesB, coordinatesInsideA) #Asssuming rectangle B is inside A
        if(resultA): #If A is partially inside B or both rectangles have a single vertex inside one another
            return str(resultA)
        elif(resultB): #If B is partially inside A, in case both rectangles have a vertex inside one another it is irrelevant whether we choose A or B
            return str(resultB)
        else: #Rectangles either do not touch or they share one vertex, or two vertices (a whole edge) or partially share an edge (and a vertex) with one rectangle facing outwards
            matchingVertices = vertexMatch(verticesA, verticesB)
            if(len(matchingVertices) == 0): #If no vertices are matching rectangles don't match
                print("Rectangles don't intersect")
            elif(len(matchingVertices) == 1): #Either their edges match partially or the rectangles only share one vertex
                verticesInEdge = edgeMatch(coordinatesInside, verticesA, verticesB)
                if(len(verticesInEdge) == 1): #If rectangles partially share an edge and a vertex
                    return "Both rectangles partially share an edge" #We could find where the edge overlap happens too but will stick to the problem requirements
                elif(len(verticesInEdge) == 2):
                    if(verticesInEdge[0] == "Top left" and verticesInEdge[1] == "Top right"): #Edges overlap at the top of rectangle B
                        return "Both rectangles share an edge at the top from vertex to vertex"
                    elif(verticesInEdge[0] == "Top right" and verticesInEdge[1] == "Bottom right"): #Edges overlap at the top of rectangle B
                        return "Both rectangles share an edge on the right from vertex to vertex"
                    elif(verticesInEdge[0] == "Bottom left" and verticesInEdge[1] == "Bottom right"): #Edges overlap at the bottom of rectangle B
                        return "Both rectangles share an edge at the bottom from vertex to vertex"
                    elif(verticesInEdge[0] == "Top left" and verticesInEdge[1] == "Bottom left"): #Edges overlap on the left side of rectangle B
                        return "Both rectangles share an edge on the left from vertex to vertex"