import math


def main():
    points = [(2,3),(2,3),(4,5),(6,7),(8,9),(11,23)]
    
    distances=[]
    
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            x = eucladian_dis(points[i], points[j])
            distances.append(x)
    
    
    minEle=100
    
    for i in range(len(distances)):
        if distances[i]<minEle:
            minEle=distances[i]
    
    print("Minimum uzaklık: ", minEle )
    
    
def eucladian_dis(point1, point2):
    distance = math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)
    
    return distance

if __name__ == "__main__":
    main()
            
        
        
