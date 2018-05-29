import cities

def test_compute_total_cities():
    x = [('Arizona', 'Phoenix', '33.448457', '-112.073844'),('Arkansas', 'Little Rock', '34.736009', '-92.331122'),('California', 'Sacramento', '38.555605', '-121.468926')]
    assert cities.compute_total_distance(x) == 3390.822869708566

def test_compute_total_cities_2():
    x = [('Virginia', 'Richmond', '37.54', '-77.46'),('Washington', 'Olympia', '47.042418', '-122.893077')]
    assert cities.compute_total_distance(x) == 4750.276634131717
    
def testcompute_total_cities_3():
    x = [('Nevada', 'Carson City', '39.160949', '-119.753877'), ('New Hampshire', 'Concord', '43.220093', '-71.549127'), ('New Jersey', 'Trenton', '40.221741', '-74.756138'), ('New Mexico', 'Santa Fe', '35.667231', '-105.964575')]
    assert cities.compute_total_distance(x) == 5262.1065106189835
    
def test_swap_adjacent_cities1():
    c = [('Alabama', 'Montgomery', '32.361538', '-86.279118'),('Alaska', 'Juneau', '58.301935', '-134.41974'), ('Arizona', 'Phoenix', '33.448457', '-112.073844')]
    dist = cities.swap_adjacent_cities(c,0)
    c == [('Alaska', 'Juneau', '58.301935', '-134.41974'),('Alabama', 'Montgomery', '32.361538', '-86.279118'),('Arizona', 'Phoenix', '33.448457', '-112.073844')]
    assert dist == ( c, 6346.559636342562)

def test_swap_adjacent_cities2():
    c = [('Alabama', 'Montgomery', '32.361538', '-86.279118'),('Alaska', 'Juneau', '58.301935', '-134.41974'), ('Arizona', 'Phoenix', '33.448457', '-112.073844')]
    dist = cities.swap_adjacent_cities(c,2)
    c == [('Arizona', 'Phoenix', '33.448457', '-112.073844'), ('Alaska', 'Juneau', '58.301935', '-134.41974'),('Alabama', 'Montgomery', '32.361538', '-86.279118')]
    assert dist == ( c, 6346.559636342563)
    
def test_swap_cities1():
  x = [('Kentucky', 'Frankfort', '38.197274', '-84.86311'), ('Louisiana', 'Baton Rouge', '30.45809', '-91.140229'),('Maine', 'Augusta', '44.323535', '-69.765261')]
  swap = cities.swap_cities(x, 1, 2)
  x = [('Kentucky', 'Frankfort', '38.197274', '-84.86311'),('Maine', 'Augusta', '44.323535', '-69.765261'), ('Louisiana', 'Baton Rouge', '30.45809', '-91.140229')]
  assert swap == (x, 3036.9277980045854)
  
def test_swap_cities2():
    x = [('Kentucky', 'Frankfort', '38.197274', '-84.86311'), ('Louisiana', 'Baton Rouge', '30.45809', '-91.140229')] 
    swap = cities.swap_cities(x, 1, 1)
    x = [('Louisiana', 'Baton Rouge', '30.45809', '-91.140229'),('Kentucky', 'Frankfort', '38.197274', '-84.86311')]
    assert swap == (x, 1285.5038285821333)
    
def test_swap_cities3():
    x = [('Kentucky', 'Frankfort', '38.197274', '-84.86311'), ('Louisiana', 'Baton Rouge', '30.45809', '-91.140229'),('Maine', 'Augusta', '44.323535', '-69.765261')]
    swap = cities.swap_cities(x, 0, 2)
    x = [('Maine', 'Augusta', '44.323535', '-69.765261'), ('Louisiana', 'Baton Rouge', '30.45809', '-91.140229'),('Kentucky', 'Frankfort', '38.197274', '-84.86311')]
    assert swap == (x, 3036.927798004586)
    
def test_swap_cities4():
  x = [('Kentucky', 'Frankfort', '38.197274', '-84.86311'), ('Louisiana', 'Baton Rouge', '30.45809', '-91.140229'),('Maine', 'Augusta', '44.323535', '-69.765261')]
  swap = cities.swap_cities(x, 1, 1)
  x = [('Kentucky', 'Frankfort', '38.197274', '-84.86311'),('Maine', 'Augusta', '44.323535', '-69.765261'),('Louisiana', 'Baton Rouge', '30.45809', '-91.140229')]
  assert swap == (x, 3036.9277980045854)
  
def test_swap_cities5():
  x = [('Kentucky', 'Frankfort', '38.197274', '-84.86311'),('Louisiana', 'Baton Rouge', '30.45809', '-91.140229'),('Maine', 'Augusta', '44.323535', '-69.765261')]
  swap = cities.swap_cities(x, 2, 2)
  x = [('Maine', 'Augusta', '44.323535', '-69.765261'),('Louisiana', 'Baton Rouge', '30.45809', '-91.140229'),('Kentucky', 'Frankfort', '38.197274', '-84.86311')]
  assert swap == (x, 3036.927798004586)


"""def test_find_best_cycle():
    x = [('London', 'Greater London', '51.509865', '-0.118092'), ('Brighton', 'Hove', '50.827930', '-0.168749'), 
         ('Portsmouth','Hampshire','50.842991', '-1.101002'), ('Southampton','Hampshire', '50.909698','-1.404351'), 
         ('Bristol', 'South Gloucestershire','51.454514','-2.587910'),('Coventry', '‎Warwickshire', '52.408310', '-1.507118')]
    x = cities.find_best_cycle(x)
    assert compute_total_distance(x) == """

def test_find_best_cycle():
    x = [('London', 'Greater London', '51.509865', '-0.118092'), ('Brighton', 'Hove', '50.827930', '-0.168749'), 
         ('Southampton','Hampshire', '50.909698','-1.404351'),('Newcastle','Tyne', '54.978754','-1.55899')]
    y = cities.find_best_cycle(x)
    assert cities.compute_total_distance(y) == 629.0768384

"""def test_find_best_cycle2():
    x = [('Truro','Cornwall','50.26526', '-5.05436'),('Edinburgh', 'Lothian' , '55.953251', '-3.188267'),
         ('Newcastle','Tyne', '54.978754','-1.55899'),('London', 'Greater London', '51.509865', '-0.118092')]
    x = cities.find_best_cycle(x)
    assert compute_total_distance(x) == """
            
def test_find_best_cycle3():
    x = [('Bath', 'Test', '51.375801','-2.359904'),('Tonbride', 'Test', '51.1953', '0.2736'),('Liverpool', 'Test', '53.41058', '-2.97794'),
         ('Shefield', 'Test','53.38297','-1.4659')]    
    y = cities.find_best_cycle(x)
    assert cities.compute_total_distance(y) == 487.5137041
