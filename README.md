<p float="left">
   <img alt="Python" src="https://img.shields.io/badge/python-%2314354C.svg?&style=for-the-badge&logo=pythonlogoColor=white"/>
   <img alt="Linux" src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black">
</p>

# Rectangles
Analyze rectangles and features that exist among rectangles (Adjacent, containment, and intersection).

## Development

The solution was developed in Python. The visualizations are created using the Matplotlib library. 

The [Point](https://github.com/aryan-goyal/Rectangles/blob/main/point.py) class contains an x and a y corrdinate which defines a point. The [Rectangle](https://github.com/aryan-goyal/Rectangles/blob/main/rectangle.py) class contains four Points and potientially a name for the rectangle. Methods for comparison for intersect, contains, adjacent proper, adjacent partial, and adjacent subline are defined within the class.

## Usage

A rectangle entity is defined by floating-point numbers on a cartesian plane. The rectangles (2 or more) can be provided in a JSON format using the following schema. Additional rectangles can be added to the list as needed for feature analysis.

```
{
    "rectangles": [
        {
            "name": "rectangle1",
            "points": [
                [0.0,0.0],
                [0.0,0.0]
            ]
        },
        {
            "name": "rectangle2",
            "points": [
                [1.0,1.0],
                [3.0,3.0]
            ]   
        }
    ] 
}
```

The reponses will be output in a JSON format similar to the following:

Example: Containment
```
{
    "rectangles": [
        {
            "rectangle1":[
                {
                    "name": "rectangle2",
                    "feature": "Containment",
                }
            ]
        }
    ] 
}
```

Example: Intersects
```
{
    "rectangles": [
        {
            "rectangle1":[
                {
                    "name": "rectangle2",
                    "feature": "Intersects",
                }
            ]
        }
    ] 
}

```

Example: Adjacent (Proper)
```
{
    "rectangles": [
        {
            "rectangle1":[
                {
                    "name": "rectangle2",
                    "feature": "Adjacent (Proper)",
                }
            ]
        }
    ] 
}
```

## Testing

## Local Setup

- On Linux or macOS, run `source setup.sh`. This will create a python virtual environment with the packages required to execute the application.

- If there is an issue related to packaging dependency, then the `pip3 -r requirements.txt` can be used to install the same package versions used for development.