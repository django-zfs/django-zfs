from django import template
register = template.Library()
from ..tools.libzfs.bindings.generic.libzfs.enums import pool_state
from ..tools.libzfs.bindings.generic.libzfs.enums import zpool_status

POOL_STATUS = {
	zpool_status.CORRUPT_CACHE: 'DANGER: Your pool contains a corrupt Cache Devices',
	zpool_status.MISSING_DEV_R: 'DANGER: Your pool is missing a device!',
	zpool_status.MISSING_DEV_NR: 'DANGER: Your pool is missing a device!',
	zpool_status.CORRUPT_LABEL_R: 'DANGER: Your pool contains a corrupt label!',
	zpool_status.CORRUPT_LABEL_NR: 'DANGER: Your pool contains a corrupt label!',
	zpool_status.BAD_GUID_SUM: 'DANGER: Your pool\'s GUID SUM is incorrect!',
	zpool_status.CORRUPT_POOL: 'DANGER: Your pool is corrupt!',
	zpool_status.FAILING_DEV: 'WARNING: Your pool contains a failing device!',
	zpool_status.VERSION_NEWER: 'DANGER: Your pool\'s on-disk version is newer than supported!',
	zpool_status.HOSTID_MISMATCH: 'WARNING: Your pool\'s Host ID doesn\'t match this system\'s Host ID!',
	zpool_status.IO_FAILURE_WAIT: 'WARNING: IO Failure!',
	zpool_status.IO_FAILURE_CONTINUE: 'WARNING: IO Failure!',
	zpool_status.BAD_LOG: 'WARNING: Your pool\'s on-disk ZFS LOG is corrupt!',
	zpool_status.ERRATA: 'WARNING: ZFS Errata warning!',
	zpool_status.UNSUP_FEAT_READ: 'WARNING: Unsupported Read Feature detected!',
	zpool_status.UNSUP_FEAT_WRITE: 'WARNING: Unsupported Write Feature detected!',
	zpool_status.FAULTED_DEV_R: 'WARNING: Faulted device device detected!',
	zpool_status.FAULTED_DEV_NR: 'WARNING: Faulted device device detected!',
	zpool_status.VERSION_OLDER: 'DANGER: The on-disk ZFS Version is lower than supported!',
	zpool_status.FEAT_DISABLED: 'WARNING: A disabled ZFS Feature has been detected!',
	zpool_status.RESILVERING: 'WARNING: This ZFS Pool is resilvering',
	zpool_status.OFFLINE_DEV: 'WARNING: This ZFS Pool has one or more offline devices!',
	zpool_status.REMOVED_DEV: 'WARNING: This ZFS Pool has one or more removed devices!',
	zpool_status.OK: 'This ZFS Pool is OK.',
}

@register.filter(name='zpoolstatus_to_string')
def zpoolstatus_to_string(status):
	return POOL_STATUS.get(status, None)
	
POOL_STATUS_TO_SEVERITY = {
	zpool_status.CORRUPT_CACHE: 'danger',
	zpool_status.MISSING_DEV_R: 'danger',
	zpool_status.MISSING_DEV_NR: 'danger',
	zpool_status.CORRUPT_LABEL_R: 'danger',
	zpool_status.CORRUPT_LABEL_NR: 'danger',
	zpool_status.BAD_GUID_SUM: 'danger',
	zpool_status.CORRUPT_POOL: 'danger',
	zpool_status.FAILING_DEV: 'warning',
	zpool_status.VERSION_NEWER: 'danger',
	zpool_status.HOSTID_MISMATCH: 'danger',
	zpool_status.IO_FAILURE_WAIT: 'warning',
	zpool_status.IO_FAILURE_CONTINUE: 'warning',
	zpool_status.BAD_LOG: 'warning',
	zpool_status.ERRATA: 'warning',
	zpool_status.UNSUP_FEAT_READ: 'warning',
	zpool_status.UNSUP_FEAT_WRITE: 'warning',
	zpool_status.FAULTED_DEV_R: 'warning',
	zpool_status.FAULTED_DEV_NR: 'warning',
	zpool_status.VERSION_OLDER: 'danger',
	zpool_status.FEAT_DISABLED: 'warning',
	zpool_status.RESILVERING: 'warning',
	zpool_status.OFFLINE_DEV: 'warning',
	zpool_status.REMOVED_DEV: 'warning',
	zpool_status.OK: 'success',
}

@register.filter(name="zpoolstatus_to_severity")
def zpoolstatus_to_severity(status):
	return POOL_STATUS_TO_SEVERITY.get(status, "info")

	
	
STATE_TO_STRING = {
				pool_state.ACTIVE : "This ZFS Pool is Active.",
				pool_state.EXPORTED : "This ZFS Pool is Exported.",
				pool_state.DESTROYED : "This ZFS Pool has been Destroyed.",
				pool_state.SPARE : "This ZFS Pool is Spare.",
				pool_state.L2CACHE : "This is a L2ARC Pool",
				pool_state.UNINITIALIZED : "This ZFS Pool is Uninitialized.",
				pool_state.UNAVAIL : "This ZFS Pool is Unavailable.",
				pool_state.POTENTIALLY_ACTIVE : "This ZFS Pool is Potentially Active."
				}

@register.filter(name="zpoolstate_to_string")
def zpoolstate_to_string(value):
	return STATE_TO_STRING.get(value, "Unknown")
	
STATE_TO_SEVERITY = {
				pool_state.ACTIVE : "success",
				pool_state.EXPORTED : "info",
				pool_state.DESTROYED : "danger",
				pool_state.SPARE : "info",
				pool_state.L2CACHE : "success",
				pool_state.UNINITIALIZED : "info",
				pool_state.UNAVAIL : "danger",
				pool_state.POTENTIALLY_ACTIVE : "warning"
				
				}

@register.filter(name="zpoolstate_to_severity")
def zpoolstate_to_severity(value):
	return STATE_TO_SEVERITY.get(value, "panel-info")