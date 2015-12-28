# coding: utf-8
# credit calculator

# dictionary containing month & days in each month
dict_month = {
    '01': 31,
    '02': 28,
    '03': 31,
    '04': 30,
    '05': 31,
    '06': 30,
    '07': 31,
    '08': 31,
    '09': 30,
    '10': 31,
    '11': 30,
    '12': 31,
}

# function containing the majority of the logic
def calc(package):

    # if package is 'e'ssentials or 'u'ltimate the issue may be only affecting one portion of the package
    if package == 'e' or package == 'u':
	    portion_of_package = raw_input("is the issue affecting the 'll', the 'bb' or 'both'? \n> ")

    #determine if isue is intermittent (total credit is halfed for that period)
    issue = raw_input("is the issue a 'c'omplete loss or an 'i'ntermittent problem? \n> ")
    start_date = raw_input("please enter the date the issue was first reported, in the format dd.mm \n> ")
    end_date = raw_input("please enter the date the issue was resolved, in the format dd.mm \n> ")

    # package price for simply broadband
    if package == 's':
	    total = 38.0
	# package price for family essentials
    elif package == 'e':
        # landline "worth" for package
	    if portion_of_package == 'll':
		    total = 35.0
		# bb "worth"
	    if portion_of_package == 'bb':
		    total = 10.0
		# total package price
	    if portion_of_package == 'both':
		    total = 45.0
    elif package == 'u':
	    if portion_of_package == 'll':
		    total = 45.0
	    if portion_of_package == 'bb':
		    total = 10.0
	    if portion_of_package == 'both':
		    total = 55.0

    # month issue first occured
    first_month = start_date[3:5]
    # month issue carried on into
    second_month = end_date[3:5]

    # first day issue reported
    first_day = float(start_date[0:2])
    # day issue was resolved
    second_day = float(end_date[0:2])

    # no of days in first month
    days_in_first_month = dict_month[first_month]
    # no of days in second month
    days_in_second_month = dict_month[second_month]

    # if months are different, calculate
    if first_month != second_month:
        # first month calculated by end of month minus day issue was reported (+1 added to include last day)
        days_without_one = (days_in_first_month + 1) - first_day
        # day issue was resolved
        days_without_two = second_day
        print '\nTHE TOTAL NUMBER OF DAYS IN %s WITHOUT SERVICE: %d\n' % (first_month, days_without_one)
        print '\nTHE TOTAL NUMBER OF DAYS IN %s WITHOUT SERVICE: %d\n' % (second_month, days_without_two)
        credit = (total / days_in_first_month * days_without_one) + (total / days_in_second_month * days_without_two)
        
        # if issue if a complete loss
        if issue == 'c':
            print "\nCREDIT DUE FOR THIS PERIOD: €%f\n" % credit
            return credit
        if issue == 'i':
            print "\nCREDIT DUE FOR THIS PERIOD: €%f\n" % (credit/2)
            return credit / 2
    else:
        days_without = (second_day - first_day) + 1
        print '\nTHE TOTAL NUMBER OF DAYS WITHOUT SERVICE: %d\n' % days_without
        credit = total / days_in_first_month * days_without
        
        if issue == 'c':
            print "CREDIT DUE FOR THIS PERIOD: €%f\n" % credit
            return credit
        if issue == 'i':
            print "CREDIT DUE FOR THIS PERIOD: €%f\n" % (credit/2)
            return credit / 2


#######################################################################################################################
# RUNTIME #
#######################################################################################################################

still_refunding = True
package = ''
credit_period = []
total_credit = 0

package = raw_input("What package are they on? 's'imply bb, 'e'ssentials or 'u'ltimate \n>")

while still_refunding:
	credit = calc(package)
	if raw_input("Do you have anymore refunds to process? 'y'es, 'n'o \n>") == 'n':
		credit_period.append(credit)
		for total in credit_period:
			total_credit += total
		print '\nTOTAL CREDIT DUE: €%f\n' % total_credit
		still_refunding = False
	else:
		credit_period.append(credit)
		print '\nPlease complete the form again for the remaining period(s)\n'
