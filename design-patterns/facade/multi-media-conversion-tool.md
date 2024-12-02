
### **Example 2: Multimedia Conversion Tool**

**Scenario:**

A multimedia application allows users to convert video files into different formats. The conversion process involves several complex subsystems:

- **Video Decoder:** Decodes the input video file.
- **Audio Extractor:** Extracts audio from the video.
- **Format Converter:** Converts video and audio into the desired output format.
- **Metadata Updater:** Updates metadata information in the output file.

**Challenge:**

- The client must coordinate multiple subsystems to perform a conversion.
- Direct interaction leads to complex code and a steep learning curve for developers.

**Solution Using the Facade Pattern:**

- Create a `MediaConverterFacade` class that provides a simple `convert_video()` method.
- The facade handles all the steps required to convert the video.

**Implementation Details:**

#### **Subsystem Classes**

**Video Decoder:**

```python
# video_decoder.py
class VideoDecoder:
    def decode(self, filename):
        print(f"Decoding video file {filename}")
        # Simulate decoding process
        return f"decoded_{filename}"
```

**Audio Extractor:**

```python
# audio_extractor.py
class AudioExtractor:
    def extract_audio(self, video_data):
        print("Extracting audio from video data")
        # Simulate audio extraction
        return "audio_stream"
```

**Format Converter:**

```python
# format_converter.py
class FormatConverter:
    def convert(self, video_data, audio_data, output_format):
        print(f"Converting video and audio to {output_format} format")
        # Simulate format conversion
        return f"converted_video.{output_format}"
```

**Metadata Updater:**

```python
# metadata_updater.py
class MetadataUpdater:
    def update_metadata(self, filename, metadata):
        print(f"Updating metadata for {filename}")
        # Simulate metadata updating
```

#### **Facade Class**

```python
# media_converter_facade.py
from video_decoder import VideoDecoder
from audio_extractor import AudioExtractor
from format_converter import FormatConverter
from metadata_updater import MetadataUpdater

class MediaConverterFacade:
    def __init__(self):
        self.decoder = VideoDecoder()
        self.audio_extractor = AudioExtractor()
        self.converter = FormatConverter()
        self.metadata_updater = MetadataUpdater()

    def convert_video(self, filename, output_format, metadata):
        print("\nStarting video conversion...")
        # Step 1: Decode Video
        video_data = self.decoder.decode(filename)

        # Step 2: Extract Audio
        audio_data = self.audio_extractor.extract_audio(video_data)

        # Step 3: Convert Format
        output_filename = self.converter.convert(video_data, audio_data, output_format)

        # Step 4: Update Metadata
        self.metadata_updater.update_metadata(output_filename, metadata)

        print(f"Video conversion completed: {output_filename}")
        return output_filename
```

**Explanation:**

- The `MediaConverterFacade` class encapsulates the conversion process.
- It provides a single method `convert_video()` to the client.
- Internally, it coordinates multiple subsystems to perform the conversion.

#### **Client Code**

```python
# client.py
from media_converter_facade import MediaConverterFacade

def main():
    converter = MediaConverterFacade()

    # Conversion details
    input_file = 'sample_video.mkv'
    output_format = 'mp4'
    metadata = {
        'title': 'Sample Video',
        'author': 'John Doe',
        'year': 2021,
    }

    # Convert the video
    converter.convert_video(input_file, output_format, metadata)

if __name__ == "__main__":
    main()
```

**Output:**

```
Starting video conversion...
Decoding video file sample_video.mkv
Extracting audio from video data
Converting video and audio to mp4 format
Updating metadata for converted_video.mp4
Video conversion completed: converted_video.mp4
```

**Benefits:**

- **User-Friendly Interface:** The client interacts with a single method to perform complex operations.
- **Modularity:** Subsystems can be modified or replaced without affecting the client code.
- **Reusability:** The facade can be used in different parts of the application or by other applications.

---