from unittest.mock import patch,mock_open

import pytest
from writers.csv import CsvWriter

@pytest.fixture
def sample_data():
    """テストで使うサンプルデータを返す"""
    return [
        {'id': '1', 'name': 'Taro', 'email': 'taro@example.com'},
        {'id': '2', 'name': '山田花子', 'email': 'hanako@example.com'}, # 日本語を含む
    ]

@pytest.fixture
def csv_writer_instance():
    """CsvWriterのインスタンスを返す"""
    return CsvWriter()

def test_write_success(csv_writer_instance, sample_data):
    m = mock_open()

    with patch('writers.csv.open', m):
        csv_writer_instance.write('test.csv', sample_data)
    m.assert_called_once_with('test.csv', 'w')

    file_handle_mock = m()
    wirten_content = "".join(call.args[0] for call in file_handle_mock.write.call_args_list)
    result_lines = wirten_content.splitlines()

    expected_lines = [
        "id,name,email",
        "1,Taro,taro@example.com",
        "2,山田花子,hanako@example.com",
    ] 
    assert result_lines == expected_lines

def test_write_failure_path_is_none(csv_writer_instance, sample_data):
    with pytest.raises(ValueError):
        csv_writer_instance.write(None, sample_data)
    
def test_write_failure_data_is_none(csv_writer_instance):
    with pytest.raises(ValueError):
        csv_writer_instance.write('test.csv', None)