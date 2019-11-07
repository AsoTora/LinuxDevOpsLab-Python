# Snapshots 
Simple python package for system monitoring.

## Description 
An app creates snapshots of the state of the system with the following data:
- Overall CPU load 
- Overall memory usage 
- Overall virtual memory usage 
- IO information 
- Network information

## Usage

### Installation
```pip install dist/snapshot-1.0-py3-none-any.whl```

Also check *requirements* for needed packages.

### Configuration
Change data format and interval time in *config.ini* file.

**Default**: Interval = 5 min, Output = txt

### Running
Import and use as any other packages:
```python
>>> import snapshot
>>> snaphot.run()
```

### Requerements
```pip install psutil```


