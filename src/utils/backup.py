"""Backup and undo operations"""

import os
import shutil
import json
from datetime import datetime
from utils.logger import Logger

logger = Logger("Backup")

class BackupManager:
    """
    Manages backup and restore operations for file changes.
    """
    
    def __init__(self, backup_dir):
        """
        Initialize backup manager.
        
        Args:
            backup_dir (str): Directory for storing backups
        """
        self.backup_dir = backup_dir
        self.metadata_file = os.path.join(backup_dir, "backups.json")
        self.backups = self._load_metadata()
        
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
    
    def _load_metadata(self):
        """
        Load backup metadata from file.
        
        Returns:
            dict: Backup metadata
        """
        if os.path.exists(self.metadata_file):
            try:
                with open(self.metadata_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                logger.error(f"Error loading backup metadata: {e}")
        return {}
    
    def _save_metadata(self):
        """
        Save backup metadata to file.
        """
        try:
            with open(self.metadata_file, 'w') as f:
                json.dump(self.backups, f, indent=2)
        except Exception as e:
            logger.error(f"Error saving backup metadata: {e}")
    
    def backup_file(self, file_path, operation_name):
        """
        Backup a file before modification.
        
        Args:
            file_path (str): Path to file to backup
            operation_name (str): Name of the operation
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if not os.path.exists(file_path):
                logger.warning(f"File not found for backup: {file_path}")
                return False
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_id = f"{operation_name}_{timestamp}"
            backup_path = os.path.join(self.backup_dir, backup_id)
            
            if os.path.isfile(file_path):
                shutil.copy2(file_path, backup_path)
            else:
                shutil.copytree(file_path, backup_path)
            
            self.backups[backup_id] = {
                "original_path": file_path,
                "backup_path": backup_path,
                "operation": operation_name,
                "timestamp": timestamp
            }
            self._save_metadata()
            logger.info(f"Backup created: {backup_id}")
            return True
            
        except Exception as e:
            logger.error(f"Error backing up file {file_path}: {e}")
            return False
    
    def restore_backup(self, backup_id):
        """
        Restore a file from backup.
        
        Args:
            backup_id (str): ID of the backup to restore
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if backup_id not in self.backups:
                logger.error(f"Backup not found: {backup_id}")
                return False
            
            backup_info = self.backups[backup_id]
            original_path = backup_info["original_path"]
            backup_path = backup_info["backup_path"]
            
            if not os.path.exists(backup_path):
                logger.error(f"Backup file not found: {backup_path}")
                return False
            
            if os.path.isfile(backup_path):
                shutil.copy2(backup_path, original_path)
            else:
                shutil.copytree(backup_path, original_path)
            
            logger.info(f"Backup restored: {backup_id}")
            return True
            
        except Exception as e:
            logger.error(f"Error restoring backup {backup_id}: {e}")
            return False
