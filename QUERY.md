
# GraphQL API Queries

This document provides examples of how to use the available GraphQL queries to fetch data from the API.




-----

## Station Queries

### Fetch a single station by ID

```graphql
query GetStation($stationId: Int!) {
  station(id: $stationId) {
    id
    alias
    city
    state
    country
    responsible
    description
  }
}
```

### Fetch all stations with pagination

```graphql
query GetStations($skip: Int, $limit: Int) {
  stations(skip: $skip, limit: $limit) {
    total_count
    page_info {
      has_next_page
      has_previous_page
    }
    edges {
      cursor
      node {
        id
        alias
        city
      }
    }
  }
}
```

### Get the total number of stations

```graphql
query GetStationTotal {
  station_total
}
```

-----

## Camera Queries

### Fetch a single camera by ID

```graphql
query GetCamera($cameraId: Int!) {
  camera(id: $cameraId) {
    id
    alias
    rtsp_url
    description
    station {
      id
      alias
    }
  }
}
```

### Fetch cameras for a specific station

```graphql
query GetCamerasByStation($stationId: Int!, $skip: Int, $limit: Int) {
  cameras_by_station(station_id: $stationId, skip: $skip, limit: $limit) {
    total_count
    edges {
      node {
        id
        alias
      }
    }
  }
}
```

### Get the total count of cameras for a station

```graphql
query GetCameraCountByStation($stationId: Int!) {
  camera_count_by_station(station_id: $stationId)
}
```

### Get the total number of all cameras

```graphql
query GetCameraTotal {
  camera_total
}
```

-----

## Sensor Queries

### Fetch a single sensor by ID

```graphql
query GetSensor($sensorId: Int!) {
  sensor(id: $sensorId) {
    id
    alias
    type
    station {
      id
      alias
    }
  }
}
```

### Fetch sensors for a specific station

```graphql
query GetSensorsByStation($stationId: Int!, $skip: Int, $limit: Int) {
  sensors_by_station(station_id: $stationId, skip: $skip, limit: $limit) {
    total_count
    edges {
      node {
        id
        alias
        type
      }
    }
  }
}
```

### Get the total count of all sensors

```graphql
query GetSensorTotal {
  sensor_total
}
```

-----

## Oblique Image Queries

### Fetch a single oblique image by ID

```graphql
query GetObliqueImage($imageId: Int!) {
  obliqueImage(id: $imageId) {
    id
    filename
    path
    timestamp
    camera {
      id
      alias
    }
  }
}
```

### Fetch oblique images for a specific camera

```graphql
query GetObliqueImagesByCamera($cameraId: Int!, $skip: Int, $limit: Int) {
  obliqueImages_by_camera(camera_id: $cameraId, skip: $skip, limit: $limit) {
    total_count
    edges {
      node {
        id
        filename
      }
    }
  }
}
```

-----

## Fusion Queries

### Fetch a single fusion by ID

```graphql
query GetFusion($fusionId: Int!) {
  fusion(id: $fusionId) {
    id
    timestamp
    fusion_type
  }
}
```

### Fetch all fusions with pagination

```graphql
query GetFusions($skip: Int, $limit: Int) {
  fusions(skip: $skip, limit: $limit) {
    total_count
    edges {
      node {
        id
        fusion_type
      }
    }
  }
}
```

-----

## Calibration Queries

### Fetch a single calibration by ID

```graphql
query GetCalibration($calId: Int!) {
  calibration(id: $calId) {
    id
    timestamp
    resolution
    EMCuv
    EMCxy
    camera {
      id
      alias
    }
  }
}
```

### Fetch calibrations for a specific camera

```graphql
query GetCalibrationsByCamera($cameraId: Int!, $skip: Int, $limit: Int) {
  calibrations_by_camera(camera_id: $cameraId, skip: $skip, limit: $limit) {
    total_count
    edges {
      node {
        id
        timestamp
      }
    }
  }
}
```

-----

## Common Point Queries

### Fetch a single common point by its composite key

```graphql
query GetCommonPoint($fusionId: Int!, $cameraId: Int!, $name: String!) {
  commonPoint(id_fusion: $fusionId, camera_id: $cameraId, name: $name) {
    name
    u
    v
    camera {
      alias
    }
  }
}
```

### Fetch common points for a specific fusion

```graphql
query GetCommonPointsByFusion($fusionId: Int!, $skip: Int, $limit: Int) {
  commonPoints_by_fusion(fusion_id: $fusionId, skip: $skip, limit: $limit) {
    edges {
      node {
        name
        u
        v
      }
    }
  }
}
```


## GCP Queries

### Fetch a single GCP by ID

```graphql
query GetGCP($gcpId: Int!) {
  gcp(id: $gcpId) {
    id
    name
    x
    y
    z
    station {
      id
      alias
    }
  }
}
```

### Fetch GCPs for a specific station

```graphql
query GetGCPsByStation($stationId: Int!, $skip: Int, $limit: Int) {
  gcps_by_station(station_id: $stationId, skip: $skip, limit: $limit) {
    total_count
    edges {
      node {
        id
        name
      }
    }
  }
}
```

### Get the total count of all GCPs

```graphql
query GetGCPTotal {
  gcp_total
}
```

-----

## Automatic Parameters Queries

### Fetch a single AutomaticParams entry by ID

```graphql
query GetAutomaticParam($paramId: Int!) {
  automatic_param(id: $paramId) {
    id
    type
    start_hour
    end_hour
    step
    station {
      id
      alias
    }
  }
}
```

### Fetch AutomaticParams for a specific station

```graphql
query GetAutomaticParamsByStation($stationId: Int!, $skip: Int, $limit: Int) {
  automatic_params_by_station(station_id: $stationId, skip: $skip, limit: $limit) {
    total_count
    edges {
      node {
        id
        type
      }
    }
  }
}
```

-----

## Rectified Image Queries

### Fetch a single rectified image by ID

```graphql
query GetRectifiedImage($imageId: Int!) {
  rectifiedImage(id: $imageId) {
    id
    filename
    path
    calibration {
      id
      timestamp
    }
  }
}
```

### Fetch rectified images for a specific calibration

```graphql
query GetRectifiedImagesByCalibration($calId: Int!, $skip: Int, $limit: Int) {
  rectifiedImages_by_calibration(calibration_id: $calId, skip: $skip, limit: $limit) {
    total_count
    edges {
      node {
        id
        filename
      }
    }
  }
}
```

-----

## TimeStack Queries

### Fetch a single timestack by its filename (Primary Key)

```graphql
query GetTimeStack($filename: String!) {
  timeStack(filename: $filename) {
    id
    filename
    path
    fps
    numFrames
  }
}
```

### Fetch timestacks for a specific camera

```graphql
query GetTimeStacksByCamera($cameraId: Int!, $skip: Int, $limit: Int) {
  timeStacks_by_camera(camera_id: $cameraId, skip: $skip, limit: $limit) {
    total_count
    edges {
      node {
        id
        filename
      }
    }
  }
}
```

-----

## Image Type Queries

### Fetch a single image type by ID

```graphql
query GetImageType($typeId: Int!) {
  imageType(id: $typeId) {
    id
    name
    description
  }
}
```

### Fetch all image types

```graphql
query GetImageTypes($skip: Int, $limit: Int) {
  imageTypes(skip: $skip, limit: $limit) {
    total_count
    edges {
      node {
        id
        name
      }
    }
  }
}
```

-----

## Merged Image Queries

### Fetch a single merged image by ID

```graphql
query GetMergedImage($imageId: Int!) {
  mergedImage(id: $imageId) {
    id
    filename
    path
    fusion {
      id
      fusion_type
    }
  }
}
```

### Fetch merged images for a specific fusion

```graphql
query GetMergedImagesByFusion($fusionId: Int!, $skip: Int, $limit: Int) {
  mergedImages_by_fusion(fusion_id: $fusionId, skip: $skip, limit: $limit) {
    total_count
    edges {
      node {
        id
        filename
      }
    }
  }
}
```

-----

## CameraByFusion Queries (Join Table)

### Fetch a single CameraByFusion entry by its composite key

```graphql
query GetCameraByFusion($fusionId: Int!, $cameraId: Int!) {
  cameraByFusion(fusion_id: $fusionId, camera_id: $cameraId) {
    sequence
    camera {
      alias
    }
    fusion {
      fusion_type
    }
  }
}
```

-----

## Fusion Parameter & Value Queries

### Fetch a single fusion parameter

```graphql
query GetFusionParameter($paramId: Int!) {
  fusionParameter(id: $paramId) {
    id
    name
    fusion {
      id
    }
  }
}
```

### Fetch values for a specific fusion parameter

```graphql
query GetFusionValues($matrixId: Int!, $skip: Int, $limit: Int) {
  fusionValues_by_parameter(matrix_id: $matrixId, skip: $skip, limit: $limit) {
    total_count
    edges {
      node {
        id_col
        id_row
        value
      }
    }
  }
}
```

-----

## Calibration Parameter & Value Queries

### Fetch a single calibration parameter

```graphql
query GetCalibrationParameter($paramId: Int!) {
  calibrationParameter(id: $paramId) {
    id
    name
    calibration {
      id
    }
  }
}
```

### Fetch values for a specific calibration parameter

```graphql
query GetCalibrationValues($paramId: Int!, $skip: Int, $limit: Int) {
  calibrationValues_by_parameter(id_param: $paramId, skip: $skip, limit: $limit) {
    total_count
    edges {
      node {
        id_col
        id_row
        value
      }
    }
  }
}
```

-----

## PickedGCP Queries (Join Table)

### Fetch a single PickedGCP entry by its composite key

```graphql
query GetPickedGCP($calId: Int!, $gcpId: Int!) {
  pickedGCP(calibration_id: $calId, gcp_id: $gcpId) {
    u
    v
    gcp {
      name
      x
      y
      z
    }
  }
}
```

-----

## ROI & Coordinate Queries

### Fetch a single ROI by ID

```graphql
query GetROI($roiId: Int!) {
  roi(id: $roiId) {
    id
    type
    timestamp
  }
}
```

### Fetch coordinates for a specific ROI

```graphql
query GetROICoordinates($roiId: Int!, $skip: Int, $limit: Int) {
  roiCoordinates_by_roi(roi_id: $roiId, skip: $skip, limit: $limit) {
    total_count
    edges {
      node {
        id
        u
        v
      }
    }
  }
}
```

-----

## Measurement & Related Queries

### Fetch a single measurement by ID

```graphql
query GetMeasurement($measurementId: Int!) {
  measurement(id: $measurementId) {
    id
    timestamp
    station {
      alias
    }
    measurement_type {
      paramname
      datatype
    }
  }
}
```

### Fetch a single measurement type by ID

```graphql
query GetMeasurementType($typeId: Int!) {
  measurementType(id: $typeId) {
    id
    paramname
    datatype
    description
    sensor {
      alias
    }
  }
}
```

### Fetch values for a specific measurement

```graphql
query GetMeasurementValues($measurementId: Int!, $skip: Int, $limit: Int) {
  measurementValues_by_measurement(measurement_id: $measurementId, skip: $skip, limit: $limit) {
    total_count
    edges {
      node {
        id_col
        id_row
        id_depth
        value
      }
    }
  }
}
```
