env=development
process=all
group=all

VPATH=/home/vagrant/.virtualenvs/CollectingFeedback/bin/activate
ANSIBLE = ansible $(group) -i devops/inventory/$(env)
ANSIBLE_PLAYBOOK = ansible-playbook -i devops/inventory/$(env)

# Match any playbook in the devops directory
% :: devops/%.yml 
	$(ANSIBLE_PLAYBOOK) $< -l $(group)

status :
	$(ANSIBLE) -s -a "supervisorctl status" 


restart start stop :
	$(ANSIBLE) -s -a "supervisorctl $(@) $(process)"

restart-supervisor :
	ansible app_servers -i devops/inventory/$(env) -m shell -s \
	-a "service supervisor stop && service supervisor start"

runLocally:
	@ pip install -r requirements.txt
	@ python manage.py runserver localhost:7777

runOnVm:
	@. $(VPATH); python manage.py runserver 0.0.0.0:9090


help:
	@echo ''
	@echo 'Usage: '
	@echo ' make <command> [option=<option_value>]...'
	@echo ''
	@echo 'Setup & Deployment:'
	@echo ' make configure		Prepare servers'
	@echo ' make deploy 		Deploy app'
	@echo ''
	@echo 'Options:  '
	@echo ' env			Inventory file (Default: development)'
	@echo ' group			Inventory subgroup (Default: all)'
	@echo ''
	@echo 'Example:'
	@echo ' make configure env=staging group=app_servers'
	@echo ''
	@echo 'Application Management:'
	@echo ' make status 		Display process states'
	@echo ' make start		Start processes'
	@echo ' make restart		Restart processes'
	@echo ' make restart-supervisor	Restart supervisord'
	@echo ''
	@echo 'Options: '
	@echo ' process		A supervisor program name or group (Default: all)'
	@echo ''
	@echo 'Example:'
	@echo ' make restart process=mobile_loans:celery'

test :
	$(ANSIBLE) -a "/home/vagrant/.virtualenvs/mobile_loans/bin/python /vagrant/manage.py test api http mobile_loans.apps.airtel_tz ussd ussdlib --settings=mobile_loans.settings.development"
