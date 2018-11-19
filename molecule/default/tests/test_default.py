import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_phploc_is_installed(host):
    f = host.file('/usr/local/bin/phploc')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
