from unittest.mock import patch, mock_open, MagicMock
import json
from backend.controller.grouping_controller import GroupingController
from backend.controller.affinity_controller import AffinityController

# Initialisation
def test_init():
    controller = GroupingController(5)
    assert controller.group_size == 5
    assert "student_list.json" in controller.student_list_path
  

#Should load student
def test_load_student_votes():
    sample_data = {
        "students": [
            {"Alice": {"Bob": 8, "Charlie": 6}},
            {"Bob": {"Alice": 7, "Charlie": 5}}
        ]
    }
    
    with patch('builtins.open', mock_open()):
        with patch('json.load', return_value=sample_data):
            controller = GroupingController(3)
            result = controller.load_student_vote_list()
            
            expected = {
                "Alice": {"Bob": 8, "Charlie": 6},
                "Bob": {"Alice": 7, "Charlie": 5}
            }
            
            assert result == expected
           

# Should return valid afinity matrix bases on students votes.
def test_build_affinity_matrix():
    controller = GroupingController(3)
    
   
    mock_votes = {
        "E1": {"E2": 8, "E3": 6},
        "E2": {"E1": 7, "E3": 5},
        "E3": {"E1": 6, "E2": 4}
    }
    
    with patch.object(controller, 'load_student_vote_list', return_value=mock_votes):
        result = controller.build_affinity_matrix()
        
       
        
        assert "E1" in result
        assert "E2" in result["E1"]
        assert result["E1"]["E2"] == 8 
        assert result["E1"]["E3"] == 6  
        assert result["E2"]["E3"] == 5  
        
      
        assert result["E2"]["E1"] == result["E1"]["E2"]
        assert result["E3"]["E1"] == result["E1"]["E3"]
        assert result["E3"]["E2"] == result["E2"]["E3"]
        
       

# should write affinity matrix in json object.
def test_write_affinity_matrix():
    controller = GroupingController(3)
 
    mock_votes = {
        "Alice": {"Bob": 9},
        "Bob": {"Alice": 7}
    }
    
    with patch.object(controller, 'load_student_vote_list', return_value=mock_votes):
        with patch('builtins.open', mock_open()) as mock_file:
            with patch('json.dump') as mock_dump:
                controller.write_affinity_matrix_in_json()
                
                
                mock_file.assert_called_once()

                mock_dump.assert_called_once()
                

                written_data = mock_dump.call_args[0][0]
                
                assert written_data["Alice"]["Bob"] == 8
                assert written_data["Bob"]["Alice"] == 8
               
    

