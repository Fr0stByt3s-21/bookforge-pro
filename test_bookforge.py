import unittest
from unittest.mock import patch, mock_open
from bookforge_core import generate_audiobook

class TestBookForge(unittest.TestCase):
    @patch('requests.post')
    @patch('builtins.open', new_callable=mock_open, read_data='test content')
    def test_generate_audiobook_voice_id(self, mock_file, mock_post):
        # Arrange
        voice_id = "test_voice_id"
        expected_url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

        # Act
        generate_audiobook(voice_id)

        # Assert
        mock_post.assert_called_once()
        args, kwargs = mock_post.call_args
        self.assertEqual(args[0], expected_url)

if __name__ == '__main__':
    unittest.main()
