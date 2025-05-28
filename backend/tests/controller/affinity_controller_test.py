
from backend.controller.affinity_controller import AffinityController


#should return valid affinity value.
def test_affinity_calculation():

    affinity = AffinityController("student1", "student2", 8, 6)
    result = affinity.get_affinity()
    
    
    assert result == 7
    
   
    affinity2 = AffinityController("student3", "student4", 9, 4)
    result2 = affinity2.get_affinity()
    
    
    assert result2 == 7
    
    affinity3 = AffinityController("abde", "hugo", 5, 5)
    result3 = affinity3.get_affinity()
    
    assert result3 == 5