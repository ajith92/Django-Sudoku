from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import sudoku
import json

@ csrf_exempt
def initial(request):
    from sudoku import logic
    if request.method == 'POST' :
        post = request.POST.copy()
        if post.has_key('ID') and post.has_key('val') : 
 	    ID = post['ID']
      	    val = int(post['val'])
            row, col = int(ID[1]), int(ID[2])
            if val == 0:
                print sudoku.logic.grid
		if sudoku.logic.grid[row][col] != 0:
                    sudoku.logic.grid[row][col] = 0
		    sudoku.logic.win_counter -= 1
		    print "del"	
		    print sudoku.logic.grid
	    else:
      	        a = sudoku.logic.check_validity(val,row,col)
                if a == True :
                    sudoku.logic.insert(val,row,col)
		    sudoku.logic.win_counter+=1
		    print val
                    print sudoku.logic.grid
		    results = {	
                                'succeed' : True,
                                #'error_message':'its a error',
                                'win' : sudoku.logic.win_counter
                               }
                    if sudoku.logic.win_counter == 9:
                	print"you win"
		    return HttpResponse(json.dumps(results),mimetype='application/json')
                else:
		    print val
                    print sudoku.logic.grid
		    results = {	
                                'succeed' : False,
                                #'error_message': 'its a error',
                                'win': sudoku.logic.win_counter
                    }
		    return HttpResponse(json.dumps(results),mimetype='application/json')
        else : #this doesnt occur
            print "Insufficient POST data (need 'ID' and 'Value'!)"
	    
    else :
	get = request.GET.copy()
        print get
        if get.has_key('val') : 
 	    val = int(get['val'])
	    if val == 1 :
		sudoku.logic.create_grid_easy()
	    if val == 2 :
		sudoku.logic.create_grid_hard()
	else :
		sudoku.logic.create_grid_easy()
	
    return render(request,'sudoku.html',sudoku.logic.table)    	    


