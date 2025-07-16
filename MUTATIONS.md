
# GraphQL API Mutations

This document provides examples of how to execute `create`, `update`, and `delete` mutations for each data model.

-----

## Station Mutations

### Create a Station

```graphql
mutation CreateStation($input: StationCreateInput!) {
  create_station(input: $input) {
    id
    alias
    city
    state
    created_at
  }
}
```

**Variables:**

```json
{
  "input": {
    "alias": "Copacabana_Bello_Norte",
    "elevation": 1450,
    "lat": 6.338,
    "lon": -75.55,
    "country": "Colombia",
    "state": "Antioquia",
    "city": "Copacabana",
    "responsible": "SIATA"
  }
}
```

### Update a Station

```graphql
mutation UpdateStation($id: Int!, $input: StationUpdateInput!) {
  update_station(id: $id, input: $input) {
    id
    alias
    responsible
    description
  }
}
```

**Variables:**

```json
{
  "id": 1,
  "input": {
    "responsible": "John Doe",
    "description": "Station updated with new responsible person."
  }
}
```

### Delete a Station

```graphql
mutation DeleteStation($id: Int!) {
  delete_station(id: $id) {
    id
    alias
  }
}
```

**Variables:**

```json
{
  "id": 1
}
```

-----

## Camera Mutations

### Create a Camera

```graphql
mutation CreateCamera($input: CameraCreateInput!) {
  create_camera(input: $input) {
    id
    alias
    port
    station {
      id
      alias
    }
  }
}
```

**Variables:**

```json
{
  "input": {
    "station_id": 1,
    "alias": "CAM-01-NORTH",
    "port": 554,
    "rtsp_url": "rtsp://user:pass@192.168.1.64/Streaming/Channels/101"
  }
}
```

### Update a Camera

```graphql
mutation UpdateCamera($id: Int!, $input: CameraUpdateInput!) {
  update_camera(id: $id, input: $input) {
    id
    alias
    description
  }
}
```

**Variables:**

```json
{
  "id": 1,
  "input": {
    "alias": "CAM-01-N",
    "description": "Facing north towards the main park."
  }
}
```

### Delete a Camera

```graphql
mutation DeleteCamera($id: Int!) {
  delete_camera(id: $id) {
    id
    alias
  }
}
```

**Variables:**

```json
{
  "id": 1
}
```

-----

## Sensor Mutations

### Create a Sensor

```graphql
mutation CreateSensor($input: SensorCreateInput!) {
  create_sensor(input: $input) {
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

**Variables:**

```json
{
  "input": {
    "station_id": 1,
    "alias": "Temperature-Probe-01",
    "type": "Thermistor",
    "description": "Primary temperature sensor."
  }
}
```

### Update a Sensor

```graphql
mutation UpdateSensor($id: Int!, $input: SensorUpdateInput!) {
  update_sensor(id: $id, input: $input) {
    id
    alias
    type
  }
}
```

**Variables:**

```json
{
  "id": 1,
  "input": {
    "type": "High-Precision Thermistor"
  }
}
```

### Delete a Sensor

```graphql
mutation DeleteSensor($id: Int!) {
  delete_sensor(id: $id) {
    id
    alias
  }
}
```

**Variables:**

```json
{
  "id": 1
}
```

-----

## GCP (Ground Control Point) Mutations

### Create a GCP

```graphql
mutation CreateGCP($input: GCPCreateInput!) {
  create_gcp(input: $input) {
    id
    name
    x
    y
    z
  }
}
```

**Variables:**

```json
{
  "input": {
    "station_id": 1,
    "name": "ControlPoint-A1",
    "x": 834510.12,
    "y": 1183290.45,
    "z": 1452.3
  }
}
```

### Update a GCP

```graphql
mutation UpdateGCP($id: Int!, $input: GCPUpdateInput!) {
  update_gcp(id: $id, input: $input) {
    id
    name
    z
  }
}
```

**Variables:**

```json
{
  "id": 1,
  "input": {
    "z": 1452.5
  }
}
```

### Delete a GCP

```graphql
mutation DeleteGCP($id: Int!) {
  delete_gcp(id: $id) {
    id
    name
  }
}
```

**Variables:**

```json
{
  "id": 1
}
```

-----

## Automatic Parameters Mutations

### Create an Automatic Parameter Set

```graphql
mutation CreateAutomaticParam($input: AutomaticParamsCreateInput!) {
  create_automatic_param(input: $input) {
    id
    type
    start_hour
    end_hour
    step
  }
}
```

**Variables:**

```json
{
  "input": {
    "station_id": 1,
    "type": "TIMEX",
    "start_hour": 8,
    "start_minute": 0,
    "end_hour": 17,
    "end_minute": 30,
    "step": 600
  }
}
```

### Update an Automatic Parameter Set

```graphql
mutation UpdateAutomaticParam($id: Int!, $input: AutomaticParamsUpdateInput!) {
  update_automatic_param(id: $id, input: $input) {
    id
    step
  }
}
```

**Variables:**

```json
{
  "id": 1,
  "input": {
    "step": 300
  }
}
```

### Delete an Automatic Parameter Set

```graphql
mutation DeleteAutomaticParam($id: Int!) {
  delete_automatic_param(id: $id) {
    id
    type
  }
}
```

**Variables:**

```json
{
  "id": 1
}
```


-----

## Oblique Image Mutations

### Create an Oblique Image

```graphql
mutation CreateObliqueImage($input: ObliqueImageCreateInput!) {
  create_oblique_image(input: $input) {
    id
    filename
    path
    camera {
      id
      alias
    }
  }
}
```

**Variables:**

```json
{
  "input": {
    "camera_id": 1,
    "image_type_id": 1,
    "filename": "oblique_20250716T130500.jpg",
    "ismini": false,
    "path": "/images/oblique/",
    "timestamp": 1752765900.0
  }
}
```

### Update an Oblique Image

```graphql
mutation UpdateObliqueImage($id: Int!, $input: ObliqueImageUpdateInput!) {
  update_oblique_image(id: $id, input: $input) {
    id
    filename
    ismini
  }
}
```

**Variables:**

```json
{
  "id": 1,
  "input": {
    "ismini": true
  }
}
```

### Delete an Oblique Image

```graphql
mutation DeleteObliqueImage($id: Int!) {
  delete_oblique_image(id: $id) {
    id
    filename
  }
}
```

**Variables:**

```json
{
  "id": 1
}
```

-----

## Rectified Image Mutations

### Create a Rectified Image

```graphql
mutation CreateRectifiedImage($input: RectifiedImageCreateInput!) {
  create_rectified_image(input: $input) {
    id
    filename
    calibration {
      id
      timestamp
    }
  }
}
```

**Variables:**

```json
{
  "input": {
    "calibration_id": 1,
    "image_type_id": 2,
    "filename": "rectified_20250716T130500.jpg",
    "ismini": false,
    "path": "/images/rectified/",
    "timestamp": 1752765900.0
  }
}
```

### Update a Rectified Image

```graphql
mutation UpdateRectifiedImage($id: Int!, $input: RectifiedImageUpdateInput!) {
  update_rectified_image(id: $id, input: $input) {
    id
    filename
    path
  }
}
```

**Variables:**

```json
{
  "id": 1,
  "input": {
    "path": "/images/rectified/archive/"
  }
}
```

### Delete a Rectified Image

```graphql
mutation DeleteRectifiedImage($id: Int!) {
  delete_rectified_image(id: $id) {
    id
    filename
  }
}
```

**Variables:**

```json
{
  "id": 1
}
```

-----

## TimeStack Mutations

### Create a TimeStack

```graphql
mutation CreateTimeStack($input: TimeStackCreateInput!) {
  create_time_stack(input: $input) {
    id
    filename
    fps
    numFrames
  }
}
```

**Variables:**

```json
{
  "input": {
    "camera_id": 1,
    "filename": "timestack_cam1_20250716.avi",
    "inittime": 1752765900.0,
    "path": "/video/timestacks/",
    "fps": 2.0,
    "numFrames": 7200
  }
}
```

### Update a TimeStack

```graphql
mutation UpdateTimeStack($filename: String!, $input: TimeStackUpdateInput!) {
  update_time_stack(filename: $filename, input: $input) {
    id
    filename
    numFrames
  }
}
```

**Variables:**

```json
{
  "filename": "timestack_cam1_20250716.avi",
  "input": {
    "numFrames": 7201
  }
}
```

### Delete a TimeStack

```graphql
mutation DeleteTimeStack($filename: String!) {
  delete_time_stack(filename: $filename) {
    id
    filename
  }
}
```

**Variables:**

```json
{
  "filename": "timestack_cam1_20250716.avi"
}
```

-----

## Image Type Mutations

### Create an Image Type

```graphql
mutation CreateImageType($input: ImageTypeCreateInput!) {
  create_image_type(input: $input) {
    id
    name
    description
  }
}
```

**Variables:**

```json
{
  "input": {
    "name": "Oblique",
    "description": "Standard oblique camera snapshot."
  }
}
```

### Update an Image Type

```graphql
mutation UpdateImageType($id: Int!, $input: ImageTypeUpdateInput!) {
  update_image_type(id: $id, input: $input) {
    id
    name
    description
  }
}
```

**Variables:**

```json
{
  "id": 1,
  "input": {
    "description": "Standard oblique camera snapshot, typically 1920x1080."
  }
}
```

### Delete an Image Type

```graphql
mutation DeleteImageType($id: Int!) {
  delete_image_type(id: $id) {
    id
    name
  }
}
```

**Variables:**

```json
{
  "id": 1
}
```

-----

## Merged Image Mutations

### Create a Merged Image

```graphql
mutation CreateMergedImage($input: MergedImageCreateInput!) {
  create_merged_image(input: $input) {
    id
    filename
    fusion {
      id
    }
  }
}
```

**Variables:**

```json
{
  "input": {
    "fusion_id": 1,
    "image_type_id": 3,
    "filename": "merged_20250716T130500.jpg",
    "ismini": false,
    "path": "/images/merged/",
    "timestamp": 1752765900.0
  }
}
```

### Update a Merged Image

```graphql
mutation UpdateMergedImage($id: Int!, $input: MergedImageUpdateInput!) {
  update_merged_image(id: $id, input: $input) {
    id
    filename
    ismini
  }
}
```

**Variables:**

```json
{
  "id": 1,
  "input": {
    "ismini": true
  }
}
```

### Delete a Merged Image

```graphql
mutation DeleteMergedImage($id: Int!) {
  delete_merged_image(id: $id) {
    id
    filename
  }
}
```

**Variables:**

```json
{
  "id": 1
}
```

-----

## Fusion Mutations

### Create a Fusion

```graphql
mutation CreateFusion($input: FusionCreateInput!) {
  create_fusion(input: $input) {
    id
    timestamp
    fusion_type
  }
}
```

**Variables:**

```json
{
  "input": {
    "timestamp": 1752765900.0,
    "fusion_type": "Standard-Merge"
  }
}
```

### Update a Fusion

```graphql
mutation UpdateFusion($id: Int!, $input: FusionUpdateInput!) {
  update_fusion(id: $id, input: $input) {
    id
    fusion_type
  }
}
```

**Variables:**

```json
{
  "id": 1,
  "input": {
    "fusion_type": "Advanced-Merge-v2"
  }
}
```

### Delete a Fusion

```graphql
mutation DeleteFusion($id: Int!) {
  delete_fusion(id: $id) {
    id
    fusion_type
  }
}
```

**Variables:**

```json
{
  "id": 1
}
```

## CameraByFusion Mutations (Join Table)

### Create a CameraByFusion Link

```graphql
mutation CreateCameraByFusion($input: CameraByFusionCreateInput!) {
  create_camera_by_fusion(input: $input) {
    fusion_id
    camera_id
    sequence
  }
}
```

**Variables:**

```json
{
  "input": {
    "fusion_id": 1,
    "camera_id": 1,
    "sequence": 0
  }
}
```

### Update a CameraByFusion Link

```graphql
mutation UpdateCameraByFusion($fusionId: Int!, $cameraId: Int!, $input: CameraByFusionUpdateInput!) {
  update_camera_by_fusion(fusion_id: $fusionId, camera_id: $cameraId, input: $input) {
    fusion_id
    camera_id
    sequence
  }
}
```

**Variables:**

```json
{
  "fusionId": 1,
  "cameraId": 1,
  "input": {
    "sequence": 1
  }
}
```

### Delete a CameraByFusion Link

```graphql
mutation DeleteCameraByFusion($fusionId: Int!, $cameraId: Int!) {
  delete_camera_by_fusion(fusion_id: $fusionId, camera_id: $cameraId) {
    fusion_id
    camera_id
  }
}
```

**Variables:**

```json
{
  "fusionId": 1,
  "cameraId": 1
}
```

-----

## Fusion Parameter Mutations

### Create a Fusion Parameter

```graphql
mutation CreateFusionParameter($input: FusionParameterCreateInput!) {
  create_fusion_parameter(input: $input) {
    id
    name
    fusion {
      id
    }
  }
}
```

**Variables:**

```json
{
  "input": {
    "id_fusion": 1,
    "name": "HomographyMatrix"
  }
}
```

### Update a Fusion Parameter

```graphql
mutation UpdateFusionParameter($id: Int!, $input: FusionParameterUpdateInput!) {
  update_fusion_parameter(id: $id, input: $input) {
    id
    name
  }
}
```

**Variables:**

```json
{
  "id": 1,
  "input": {
    "name": "HomographyMatrix_v2"
  }
}
```

### Delete a Fusion Parameter

```graphql
mutation DeleteFusionParameter($id: Int!) {
  delete_fusion_parameter(id: $id) {
    id
    name
  }
}
```

**Variables:**

```json
{
  "id": 1
}
```

-----

## Fusion Value Mutations

### Create a Fusion Value

```graphql
mutation CreateFusionValue($input: FusionValueCreateInput!) {
  create_fusion_value(input: $input) {
    matrix_id
    id_col
    id_row
    value
  }
}
```

**Variables:**

```json
{
  "input": {
    "matrix_id": 1,
    "id_col": 0,
    "id_row": 0,
    "value": 1.2345
  }
}
```

### Update a Fusion Value

```graphql
mutation UpdateFusionValue($matrixId: Int!, $idCol: Int!, $idRow: Int!, $input: FusionValueUpdateInput!) {
  update_fusion_value(matrix_id: $matrixId, id_col: $idCol, id_row: $idRow, input: $input) {
    matrix_id
    id_col
    id_row
    value
  }
}
```

**Variables:**

```json
{
  "matrixId": 1,
  "idCol": 0,
  "idRow": 0,
  "input": {
    "value": 1.2350
  }
}
```

### Delete a Fusion Value

```graphql
mutation DeleteFusionValue($matrixId: Int!, $idCol: Int!, $idRow: Int!) {
  delete_fusion_value(matrix_id: $matrixId, id_col: $idCol, id_row: $idRow) {
    matrix_id
    id_col
    id_row
  }
}
```

**Variables:**

```json
{
  "matrixId": 1,
  "idCol": 0,
  "idRow": 0
}
```

-----

## Common Point Mutations

### Create a Common Point

```graphql
mutation CreateCommonPoint($input: CommonPointCreateInput!) {
  create_common_point(input: $input) {
    name
    u
    v
  }
}
```

**Variables:**

```json
{
  "input": {
    "id_fusion": 1,
    "camera_id": 1,
    "name": "Corner-A",
    "u": 1024.5,
    "v": 768.2
  }
}
```

### Update a Common Point

```graphql
mutation UpdateCommonPoint($idFusion: Int!, $cameraId: Int!, $name: String!, $input: CommonPointUpdateInput!) {
  update_common_point(id_fusion: $idFusion, camera_id: $cameraId, name: $name, input: $input) {
    name
    u
    v
  }
}
```

**Variables:**

```json
{
  "idFusion": 1,
  "cameraId": 1,
  "name": "Corner-A",
  "input": {
    "u": 1025.0
  }
}
```

### Delete a Common Point

```graphql
mutation DeleteCommonPoint($idFusion: Int!, $cameraId: Int!, $name: String!) {
  delete_common_point(id_fusion: $idFusion, camera_id: $cameraId, name: $name) {
    name
  }
}
```

**Variables:**

```json
{
  "idFusion": 1,
  "cameraId": 1,
  "name": "Corner-A"
}
```

-----

## Calibration Mutations

### Create a Calibration

```graphql
mutation CreateCalibration($input: CalibrationCreateInput!) {
  create_calibration(input: $input) {
    id
    timestamp
    resolution
  }
}
```

**Variables:**

```json
{
  "input": {
    "camera_id": 1,
    "timestamp": 1752765900.0,
    "resolution": 0.95
  }
}
```

### Update a Calibration

```graphql
mutation UpdateCalibration($id: Int!, $input: CalibrationUpdateInput!) {
  update_calibration(id: $id, input: $input) {
    id
    EMCuv
    EMCxy
  }
}
```

**Variables:**

```json
{
  "id": 1,
  "input": {
    "EMCuv": 0.5,
    "EMCxy": 0.45
  }
}
```

### Delete a Calibration

```graphql
mutation DeleteCalibration($id: Int!) {
  delete_calibration(id: $id) {
    id
    timestamp
  }
}
```

**Variables:**

```json
{
  "id": 1
}
```

-----

## Calibration Parameter Mutations

### Create a Calibration Parameter

```graphql
mutation CreateCalibrationParameter($input: CalibrationParameterCreateInput!) {
  create_calibration_parameter(input: $input) {
    id
    name
  }
}
```

**Variables:**

```json
{
  "input": {
    "calibration_id": 1,
    "name": "IntrinsicMatrix"
  }
}
```

### Update a Calibration Parameter

```graphql
mutation UpdateCalibrationParameter($id: Int!, $input: CalibrationParameterUpdateInput!) {
  update_calibration_parameter(id: $id, input: $input) {
    id
    name
  }
}
```

**Variables:**

```json
{
  "id": 1,
  "input": {
    "name": "IntrinsicMatrix_v2"
  }
}
```

### Delete a Calibration Parameter

```graphql
mutation DeleteCalibrationParameter($id: Int!) {
  delete_calibration_parameter(id: $id) {
    id
    name
  }
}
```

**Variables:**

```json
{
  "id": 1
}
```

-----

## Calibration Value Mutations

### Create a Calibration Value

```graphql
mutation CreateCalibrationValue($input: CalibrationValueCreateInput!) {
  create_calibration_value(input: $input) {
    id_param
    id_col
    id_row
    value
  }
}
```

**Variables:**

```json
{
  "input": {
    "id_param": 1,
    "id_col": 0,
    "id_row": 0,
    "value": 1500.123
  }
}
```

### Update a Calibration Value

```graphql
mutation UpdateCalibrationValue($idParam: Int!, $idCol: Int!, $idRow: Int!, $input: CalibrationValueUpdateInput!) {
  update_calibration_value(id_param: $idParam, id_col: $idCol, id_row: $idRow, input: $input) {
    id_param
    id_col
    id_row
    value
  }
}
```

**Variables:**

```json
{
  "idParam": 1,
  "idCol": 0,
  "idRow": 0,
  "input": {
    "value": 1501.0
  }
}
```

### Delete a Calibration Value

```graphql
mutation DeleteCalibrationValue($idParam: Int!, $idCol: Int!, $idRow: Int!) {
  delete_calibration_value(id_param: $idParam, id_col: $idCol, id_row: $idRow) {
    id_param
    id_col
    id_row
  }
}
```

**Variables:**

```json
{
  "idParam": 1,
  "idCol": 0,
  "idRow": 0
}
```

## CameraByFusion Mutations (Join Table)

### Create a CameraByFusion Link

```graphql
mutation CreateCameraByFusion($input: CameraByFusionCreateInput!) {
  create_camera_by_fusion(input: $input) {
    fusion_id
    camera_id
    sequence
  }
}
```

**Variables:**

```json
{
  "input": {
    "fusion_id": 1,
    "camera_id": 1,
    "sequence": 0
  }
}
```

### Update a CameraByFusion Link

```graphql
mutation UpdateCameraByFusion($fusionId: Int!, $cameraId: Int!, $input: CameraByFusionUpdateInput!) {
  update_camera_by_fusion(fusion_id: $fusionId, camera_id: $cameraId, input: $input) {
    fusion_id
    camera_id
    sequence
  }
}
```

**Variables:**

```json
{
  "fusionId": 1,
  "cameraId": 1,
  "input": {
    "sequence": 1
  }
}
```

### Delete a CameraByFusion Link

```graphql
mutation DeleteCameraByFusion($fusionId: Int!, $cameraId: Int!) {
  delete_camera_by_fusion(fusion_id: $fusionId, camera_id: $cameraId) {
    fusion_id
    camera_id
  }
}
```

**Variables:**

```json
{
  "fusionId": 1,
  "cameraId": 1
}
```

-----

## Fusion Parameter Mutations

### Create a Fusion Parameter

```graphql
mutation CreateFusionParameter($input: FusionParameterCreateInput!) {
  create_fusion_parameter(input: $input) {
    id
    name
    fusion {
      id
    }
  }
}
```

**Variables:**

```json
{
  "input": {
    "id_fusion": 1,
    "name": "HomographyMatrix"
  }
}
```

### Update a Fusion Parameter

```graphql
mutation UpdateFusionParameter($id: Int!, $input: FusionParameterUpdateInput!) {
  update_fusion_parameter(id: $id, input: $input) {
    id
    name
  }
}
```

**Variables:**

```json
{
  "id": 1,
  "input": {
    "name": "HomographyMatrix_v2"
  }
}
```

### Delete a Fusion Parameter

```graphql
mutation DeleteFusionParameter($id: Int!) {
  delete_fusion_parameter(id: $id) {
    id
    name
  }
}
```

**Variables:**

```json
{
  "id": 1
}
```

-----

## Fusion Value Mutations

### Create a Fusion Value

```graphql
mutation CreateFusionValue($input: FusionValueCreateInput!) {
  create_fusion_value(input: $input) {
    matrix_id
    id_col
    id_row
    value
  }
}
```

**Variables:**

```json
{
  "input": {
    "matrix_id": 1,
    "id_col": 0,
    "id_row": 0,
    "value": 1.2345
  }
}
```

### Update a Fusion Value

```graphql
mutation UpdateFusionValue($matrixId: Int!, $idCol: Int!, $idRow: Int!, $input: FusionValueUpdateInput!) {
  update_fusion_value(matrix_id: $matrixId, id_col: $idCol, id_row: $idRow, input: $input) {
    matrix_id
    id_col
    id_row
    value
  }
}
```

**Variables:**

```json
{
  "matrixId": 1,
  "idCol": 0,
  "idRow": 0,
  "input": {
    "value": 1.2350
  }
}
```

### Delete a Fusion Value

```graphql
mutation DeleteFusionValue($matrixId: Int!, $idCol: Int!, $idRow: Int!) {
  delete_fusion_value(matrix_id: $matrixId, id_col: $idCol, id_row: $idRow) {
    matrix_id
    id_col
    id_row
  }
}
```

**Variables:**

```json
{
  "matrixId": 1,
  "idCol": 0,
  "idRow": 0
}
```

-----

## Common Point Mutations

### Create a Common Point

```graphql
mutation CreateCommonPoint($input: CommonPointCreateInput!) {
  create_common_point(input: $input) {
    name
    u
    v
  }
}
```

**Variables:**

```json
{
  "input": {
    "id_fusion": 1,
    "camera_id": 1,
    "name": "Corner-A",
    "u": 1024.5,
    "v": 768.2
  }
}
```

### Update a Common Point

```graphql
mutation UpdateCommonPoint($idFusion: Int!, $cameraId: Int!, $name: String!, $input: CommonPointUpdateInput!) {
  update_common_point(id_fusion: $idFusion, camera_id: $cameraId, name: $name, input: $input) {
    name
    u
    v
  }
}
```

**Variables:**

```json
{
  "idFusion": 1,
  "cameraId": 1,
  "name": "Corner-A",
  "input": {
    "u": 1025.0
  }
}
```

### Delete a Common Point

```graphql
mutation DeleteCommonPoint($idFusion: Int!, $cameraId: Int!, $name: String!) {
  delete_common_point(id_fusion: $idFusion, camera_id: $cameraId, name: $name) {
    name
  }
}
```

**Variables:**

```json
{
  "idFusion": 1,
  "cameraId": 1,
  "name": "Corner-A"
}
```

-----

## Calibration Mutations

### Create a Calibration

```graphql
mutation CreateCalibration($input: CalibrationCreateInput!) {
  create_calibration(input: $input) {
    id
    timestamp
    resolution
  }
}
```

**Variables:**

```json
{
  "input": {
    "camera_id": 1,
    "timestamp": 1752765900.0,
    "resolution": 0.95
  }
}
```

### Update a Calibration

```graphql
mutation UpdateCalibration($id: Int!, $input: CalibrationUpdateInput!) {
  update_calibration(id: $id, input: $input) {
    id
    EMCuv
    EMCxy
  }
}
```

**Variables:**

```json
{
  "id": 1,
  "input": {
    "EMCuv": 0.5,
    "EMCxy": 0.45
  }
}
```

### Delete a Calibration

```graphql
mutation DeleteCalibration($id: Int!) {
  delete_calibration(id: $id) {
    id
    timestamp
  }
}
```

**Variables:**

```json
{
  "id": 1
}
```

-----

## Calibration Parameter Mutations

### Create a Calibration Parameter

```graphql
mutation CreateCalibrationParameter($input: CalibrationParameterCreateInput!) {
  create_calibration_parameter(input: $input) {
    id
    name
  }
}
```

**Variables:**

```json
{
  "input": {
    "calibration_id": 1,
    "name": "IntrinsicMatrix"
  }
}
```

### Update a Calibration Parameter

```graphql
mutation UpdateCalibrationParameter($id: Int!, $input: CalibrationParameterUpdateInput!) {
  update_calibration_parameter(id: $id, input: $input) {
    id
    name
  }
}
```

**Variables:**

```json
{
  "id": 1,
  "input": {
    "name": "IntrinsicMatrix_v2"
  }
}
```

### Delete a Calibration Parameter

```graphql
mutation DeleteCalibrationParameter($id: Int!) {
  delete_calibration_parameter(id: $id) {
    id
    name
  }
}
```

**Variables:**

```json
{
  "id": 1
}
```

-----

## Calibration Value Mutations

### Create a Calibration Value

```graphql
mutation CreateCalibrationValue($input: CalibrationValueCreateInput!) {
  create_calibration_value(input: $input) {
    id_param
    id_col
    id_row
    value
  }
}
```

**Variables:**

```json
{
  "input": {
    "id_param": 1,
    "id_col": 0,
    "id_row": 0,
    "value": 1500.123
  }
}
```

### Update a Calibration Value

```graphql
mutation UpdateCalibrationValue($idParam: Int!, $idCol: Int!, $idRow: Int!, $input: CalibrationValueUpdateInput!) {
  update_calibration_value(id_param: $idParam, id_col: $idCol, id_row: $idRow, input: $input) {
    id_param
    id_col
    id_row
    value
  }
}
```

**Variables:**

```json
{
  "idParam": 1,
  "idCol": 0,
  "idRow": 0,
  "input": {
    "value": 1501.0
  }
}
```

### Delete a Calibration Value

```graphql
mutation DeleteCalibrationValue($idParam: Int!, $idCol: Int!, $idRow: Int!) {
  delete_calibration_value(id_param: $idParam, id_col: $idCol, id_row: $idRow) {
    id_param
    id_col
    id_row
  }
}
```

**Variables:**

```json
{
  "idParam": 1,
  "idCol": 0,
  "idRow": 0
}
```