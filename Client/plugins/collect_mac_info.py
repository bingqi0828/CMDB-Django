import subprocess

def collect():
    raw_data={}
    
    filter_keys = ['Manufacturer', 'Serial Number', 'Product Name', 'UUID', 'Wake-up Type']

    for key in filter_keys:
        try:
            cmd1 = "/usr/sbin/system_profiler SPHardwareDataType|grep '%s'" % key
            result=subprocess.Popen(cmd1, stdout=subprocess.PIPE, shell=True).stdout.read().decode()
            data_list = result.split(':')
            if(len(data_list) >1):
                raw_data[key]=data_list[1].strip()
            else:
                raw_data[key]=''
        except Exception as e:
            print (e)
            raw_data[key]=''

    data = dict()
    data['asset_type'] = 'server'
    data['manufacturer'] = raw_data['Manufacturer']
    data['sn'] = raw_data['Serial Number']
    data['model'] = raw_data['Product Name']
    data['uuid'] = raw_data['UUID']
    data['wake_up_type'] = raw_data['Wake-up Type']

    data.update(get_os_info())
    #data.update(get_cpu_info())
    #data.update(get_ram_info())
    #data.update(get_nic_info())
    #data.update(get_disk_info())
    return data

def get_os_info():
    cmd1 = "sw_vers|grep 'ProductVersion'" 
    result=subprocess.Popen(cmd1, stdout=subprocess.PIPE, shell=True).stdout.read().decode()
    
    data_dict={
        "os_distribution":"",
        "os_release": result.split(':')[1].strip(),
        "os_type": "MacOs",
    }
    return data_dict

def get_cpu_info():
    return 

def get_ram_info():
    return 

def get_nic_info():
    return 

def get_disk_info():
    return 

if __name__=='__main__':
    data=collect()
    print(data)