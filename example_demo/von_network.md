TRUNCATED

```bash
node1-1      | 2024-09-11 17:19:23,960|INFO|consensus_shared_data.py|Node1:0 updated validators list to {'Node4', 'Node3', 'Node1', 'Node2'}
node1-1      | 2024-09-11 17:19:23,960|INFO|consensus_shared_data.py|Node1:1 updated validators list to {'Node4', 'Node3', 'Node1', 'Node2'}
node1-1      | 2024-09-11 17:19:23,960|INFO|replica.py|Node1:0 setting primaryName for view no 0 to: Node1:0
node1-1      | 2024-09-11 17:19:23,961|NOTIFICATION|primary_connection_monitor_service.py|Node1:0 restored connection to primary of master
node1-1      | 2024-09-11 17:19:23,961|NOTIFICATION|node.py|PRIMARY SELECTION:  selected primary Node1:0 for instance 0 (view 0)
node1-1      | 2024-09-11 17:19:23,961|INFO|replica.py|Node1:1 setting primaryName for view no 0 to: Node2:1
node1-1      | 2024-09-11 17:19:23,961|INFO|node.py|Node1 scheduling replica removal for instance 1 in 180 sec
node1-1      | 2024-09-11 17:19:23,961|NOTIFICATION|node.py|PRIMARY SELECTION:  selected primary Node2:1 for instance 1 (view 0)
node1-1      | 2024-09-11 17:19:23,961|INFO|node.py|Node1 started participating
node1-1      | 2024-09-11 17:19:23,961|INFO|checkpoint_service.py|update_watermark_from_3pc to (0, 3)
node1-1      | 2024-09-11 17:19:23,961|INFO|checkpoint_service.py|Node1:0 - checkpoint_service set watermarks as 3 303
node1-1      | 2024-09-11 17:19:23,961|INFO|checkpoint_service.py|Node1:1 - checkpoint_service set watermarks as 0 9223372036854775807
node1-1      | 2024-09-11 17:19:23,961|INFO|last_sent_pp_store_helper.py|Node1 trying to restore lastPrePrepareSeqNo
node1-1      | 2024-09-11 17:19:23,962|INFO|last_sent_pp_store_helper.py|Node1 did not find stored lastSentPrePrepare
node1-1      | 2024-09-11 17:19:23,962|INFO|last_sent_pp_store_helper.py|Node1 erasing stored lastSentPrePrepare
node1-1      | 2024-09-11 17:19:23,962|INFO|zstack.py|Processing messages from previously unknown remotes.
node3-1      | 2024-09-11 17:19:23,968|INFO|seeder_service.py|Node3 received ledger status: LEDGER_STATUS{'ledgerId': 0, 'txnSeqNo': 4, 'viewNo': None, 'ppSeqNo': None, 'merkleRoot': 'Cv3r9P26vvuKDekhaHSSUW1mBRihUSgTZcAzhmgAMa1A', 'protocolVersion': 2} from Node2
node3-1      | 2024-09-11 17:19:23,969|INFO|cons_proof_service.py|Node3:ConsProofService:0 comparing its ledger 0 of size 4 with 4
node3-1      | 2024-09-11 17:19:23,969|INFO|cons_proof_service.py|Node3:ConsProofService:0 comparing its ledger 0 of size 4 with 4
node3-1      | 2024-09-11 17:19:23,969|INFO|cons_proof_service.py|Node3:ConsProofService:0 finished with consistency proof None
node3-1      | 2024-09-11 17:19:23,970|INFO|catchup_rep_service.py|Node3:CatchupRepService:0 started catching up with LedgerCatchupStart(ledger_id=0, catchup_till=None, nodes_ledger_sizes={})
node3-1      | 2024-09-11 17:19:23,970|INFO|catchup_rep_service.py|CATCH-UP: Node3:CatchupRepService:0 completed catching up ledger 0, caught up 0 in total
node3-1      | 2024-09-11 17:19:23,970|INFO|node_leecher_service.py|Node3:NodeLeecherService transitioning from PreSyncingPool to SyncingAudit
node3-1      | 2024-09-11 17:19:23,970|INFO|cons_proof_service.py|Node3:ConsProofService:3 starts
node3-1      | 2024-09-11 17:19:23,970|INFO|cons_proof_service.py|Node3:ConsProofService:3 asking for ledger status of ledger 3
node3-1      | 2024-09-11 17:19:23,971|NOTIFICATION|keep_in_touch.py|Node3's connections changed from {'Node1'} to {'Node1', 'Node2'}
node3-1      | 2024-09-11 17:19:23,971|NOTIFICATION|keep_in_touch.py|CONNECTION: Node3 now connected to Node2
node3-1      | 2024-09-11 17:19:23,971|INFO|motor.py|Node3 changing status from starting to started_hungry
node3-1      | 2024-09-11 17:19:23,971|INFO|primary_connection_monitor_service.py|Node3:1 scheduling primary connection check in 60 sec
node4-1      | 2024-09-11 17:19:23,972|NOTIFICATION|keep_in_touch.py|Node4's connections changed from {'Node3', 'Node1'} to {'Node3', 'Node2', 'Node1'}
node4-1      | 2024-09-11 17:19:23,972|NOTIFICATION|keep_in_touch.py|CONNECTION: Node4 now connected to Node2
node4-1      | 2024-09-11 17:19:23,973|INFO|motor.py|Node4 changing status from started_hungry to started
node1-1      | 2024-09-11 17:19:23,976|INFO|seeder_service.py|Node1 received ledger status: LEDGER_STATUS{'ledgerId': 3, 'txnSeqNo': 3, 'viewNo': None, 'ppSeqNo': None, 'merkleRoot': 'Hz5MC1sTjUFSgHaefctzCah7g752HmDqrN816PtC6tJD', 'protocolVersion': 2} from Node2
node1-1      | 2024-09-11 17:19:23,976|INFO|cons_proof_service.py|Node1:ConsProofService:3 ignoring LEDGER_STATUS{'ledgerId': 3, 'txnSeqNo': 3, 'viewNo': None, 'ppSeqNo': None, 'merkleRoot': 'Hz5MC1sTjUFSgHaefctzCah7g752HmDqrN816PtC6tJD', 'protocolVersion': 2} since it is not gathering ledger statuses
node1-1      | 2024-09-11 17:19:23,976|INFO|seeder_service.py|Node1 received ledger status: LEDGER_STATUS{'ledgerId': 0, 'txnSeqNo': 4, 'viewNo': None, 'ppSeqNo': None, 'merkleRoot': 'Cv3r9P26vvuKDekhaHSSUW1mBRihUSgTZcAzhmgAMa1A', 'protocolVersion': 2} from Node2
node1-1      | 2024-09-11 17:19:23,976|INFO|cons_proof_service.py|Node1:ConsProofService:0 ignoring LEDGER_STATUS{'ledgerId': 0, 'txnSeqNo': 4, 'viewNo': None, 'ppSeqNo': None, 'merkleRoot': 'Cv3r9P26vvuKDekhaHSSUW1mBRihUSgTZcAzhmgAMa1A', 'protocolVersion': 2} since it is not gathering ledger statuses
node1-1      | 2024-09-11 17:19:23,977|NOTIFICATION|keep_in_touch.py|Node1's connections changed from {'Node4', 'Node3'} to {'Node4', 'Node3', 'Node2'}
node1-1      | 2024-09-11 17:19:23,977|NOTIFICATION|keep_in_touch.py|CONNECTION: Node1 now connected to Node2
node1-1      | 2024-09-11 17:19:23,977|INFO|motor.py|Node1 changing status from started_hungry to started
node2-1      | 2024-09-11 17:19:23,981|INFO|seeder_service.py|Node2 received ledger status: LEDGER_STATUS{'ledgerId': 0, 'txnSeqNo': 4, 'viewNo': None, 'ppSeqNo': None, 'merkleRoot': 'Cv3r9P26vvuKDekhaHSSUW1mBRihUSgTZcAzhmgAMa1A', 'protocolVersion': 2} from Node4
node2-1      | 2024-09-11 17:19:23,981|INFO|cons_proof_service.py|Node2:ConsProofService:0 comparing its ledger 0 of size 4 with 4
node2-1      | 2024-09-11 17:19:23,981|INFO|cons_proof_service.py|Node2:ConsProofService:0 comparing its ledger 0 of size 4 with 4
node2-1      | 2024-09-11 17:19:23,981|INFO|seeder_service.py|Node2 received ledger status: LEDGER_STATUS{'ledgerId': 0, 'txnSeqNo': 4, 'viewNo': None, 'ppSeqNo': None, 'merkleRoot': 'Cv3r9P26vvuKDekhaHSSUW1mBRihUSgTZcAzhmgAMa1A', 'protocolVersion': 2} from Node1
node2-1      | 2024-09-11 17:19:23,981|INFO|cons_proof_service.py|Node2:ConsProofService:0 comparing its ledger 0 of size 4 with 4
node2-1      | 2024-09-11 17:19:23,981|INFO|cons_proof_service.py|Node2:ConsProofService:0 comparing its ledger 0 of size 4 with 4
node2-1      | 2024-09-11 17:19:23,982|INFO|cons_proof_service.py|Node2:ConsProofService:0 finished with consistency proof None
node2-1      | 2024-09-11 17:19:23,982|INFO|catchup_rep_service.py|Node2:CatchupRepService:0 started catching up with LedgerCatchupStart(ledger_id=0, catchup_till=None, nodes_ledger_sizes={})
node2-1      | 2024-09-11 17:19:23,982|INFO|catchup_rep_service.py|CATCH-UP: Node2:CatchupRepService:0 completed catching up ledger 0, caught up 0 in total
node2-1      | 2024-09-11 17:19:23,982|INFO|node_leecher_service.py|Node2:NodeLeecherService transitioning from PreSyncingPool to SyncingAudit
node2-1      | 2024-09-11 17:19:23,982|INFO|cons_proof_service.py|Node2:ConsProofService:3 starts
node2-1      | 2024-09-11 17:19:23,983|INFO|cons_proof_service.py|Node2:ConsProofService:3 asking for ledger status of ledger 3
node2-1      | 2024-09-11 17:19:23,983|INFO|seeder_service.py|Node2 received ledger status: LEDGER_STATUS{'ledgerId': 0, 'txnSeqNo': 4, 'viewNo': None, 'ppSeqNo': None, 'merkleRoot': 'Cv3r9P26vvuKDekhaHSSUW1mBRihUSgTZcAzhmgAMa1A', 'protocolVersion': 2} from Node3
node2-1      | 2024-09-11 17:19:23,983|INFO|cons_proof_service.py|Node2:ConsProofService:0 ignoring LEDGER_STATUS{'ledgerId': 0, 'txnSeqNo': 4, 'viewNo': None, 'ppSeqNo': None, 'merkleRoot': 'Cv3r9P26vvuKDekhaHSSUW1mBRihUSgTZcAzhmgAMa1A', 'protocolVersion': 2} since it is not gathering ledger statuses
node2-1      | 2024-09-11 17:19:23,984|NOTIFICATION|keep_in_touch.py|Node2's connections changed from {'Node3', 'Node1'} to {'Node3', 'Node4', 'Node1'}
node2-1      | 2024-09-11 17:19:23,984|NOTIFICATION|keep_in_touch.py|CONNECTION: Node2 now connected to Node4
node2-1      | 2024-09-11 17:19:23,984|INFO|motor.py|Node2 changing status from started_hungry to started
node3-1      | 2024-09-11 17:19:23,986|INFO|seeder_service.py|Node3 received ledger status: LEDGER_STATUS{'ledgerId': 3, 'txnSeqNo': 3, 'viewNo': None, 'ppSeqNo': None, 'merkleRoot': 'Hz5MC1sTjUFSgHaefctzCah7g752HmDqrN816PtC6tJD', 'protocolVersion': 2} from Node1
node3-1      | 2024-09-11 17:19:23,986|INFO|cons_proof_service.py|Node3:ConsProofService:3 comparing its ledger 3 of size 3 with 3
node3-1      | 2024-09-11 17:19:23,986|INFO|cons_proof_service.py|Node3:ConsProofService:3 comparing its ledger 3 of size 3 with 3
node3-1      | 2024-09-11 17:19:23,986|INFO|seeder_service.py|Node3 received ledger status: LEDGER_STATUS{'ledgerId': 3, 'txnSeqNo': 3, 'viewNo': None, 'ppSeqNo': None, 'merkleRoot': 'Hz5MC1sTjUFSgHaefctzCah7g752HmDqrN816PtC6tJD', 'protocolVersion': 2} from Node2
node3-1      | 2024-09-11 17:19:23,986|INFO|cons_proof_service.py|Node3:ConsProofService:3 comparing its ledger 3 of size 3 with 3
node3-1      | 2024-09-11 17:19:23,986|INFO|cons_proof_service.py|Node3:ConsProofService:3 comparing its ledger 3 of size 3 with 3
node3-1      | 2024-09-11 17:19:23,987|INFO|cons_proof_service.py|Node3:ConsProofService:3 finished with consistency proof None
node3-1      | 2024-09-11 17:19:23,987|INFO|catchup_rep_service.py|Node3:CatchupRepService:3 started catching up with LedgerCatchupStart(ledger_id=3, catchup_till=None, nodes_ledger_sizes={})
node3-1      | 2024-09-11 17:19:23,987|INFO|catchup_rep_service.py|CATCH-UP: Node3:CatchupRepService:3 completed catching up ledger 3, caught up 0 in total
node3-1      | 2024-09-11 17:19:23,987|INFO|node_leecher_service.py|Node3:NodeLeecherService transitioning from SyncingAudit to SyncingPool
node3-1      | 2024-09-11 17:19:23,987|INFO|catchup_rep_service.py|Node3:CatchupRepService:0 started catching up with LedgerCatchupStart(ledger_id=0, catchup_till=None, nodes_ledger_sizes={})
node3-1      | 2024-09-11 17:19:23,987|INFO|catchup_rep_service.py|CATCH-UP: Node3:CatchupRepService:0 completed catching up ledger 0, caught up 0 in total
node3-1      | 2024-09-11 17:19:23,987|INFO|node_leecher_service.py|Node3:NodeLeecherService transitioning from SyncingPool to SyncingConfig
node3-1      | 2024-09-11 17:19:23,988|INFO|catchup_rep_service.py|Node3:CatchupRepService:2 started catching up with LedgerCatchupStart(ledger_id=2, catchup_till=None, nodes_ledger_sizes={})
node3-1      | 2024-09-11 17:19:23,988|INFO|catchup_rep_service.py|CATCH-UP: Node3:CatchupRepService:2 completed catching up ledger 2, caught up 0 in total
node3-1      | 2024-09-11 17:19:23,988|INFO|node_leecher_service.py|Node3:NodeLeecherService transitioning from SyncingConfig to SyncingOthers
node4-1      | 2024-09-11 17:19:23,988|INFO|seeder_service.py|Node4 received ledger status: LEDGER_STATUS{'ledgerId': 0, 'txnSeqNo': 4, 'viewNo': None, 'ppSeqNo': None, 'merkleRoot': 'Cv3r9P26vvuKDekhaHSSUW1mBRihUSgTZcAzhmgAMa1A', 'protocolVersion': 2} from Node2
node4-1      | 2024-09-11 17:19:23,988|INFO|cons_proof_service.py|Node4:ConsProofService:0 comparing its ledger 0 of size 4 with 4
node3-1      | 2024-09-11 17:19:23,988|INFO|catchup_rep_service.py|Node3:CatchupRepService:1 started catching up with LedgerCatchupStart(ledger_id=1, catchup_till=None, nodes_ledger_sizes={})
node3-1      | 2024-09-11 17:19:23,988|INFO|catchup_rep_service.py|CATCH-UP: Node3:CatchupRepService:1 completed catching up ledger 1, caught up 0 in total
node4-1      | 2024-09-11 17:19:23,988|INFO|cons_proof_service.py|Node4:ConsProofService:0 comparing its ledger 0 of size 4 with 4
node3-1      | 2024-09-11 17:19:23,988|INFO|node_leecher_service.py|Node3:NodeLeecherService transitioning from SyncingOthers to Idle
node3-1      | 2024-09-11 17:19:23,988|INFO|node.py|Node3 caught up to 0 txns in the last catchup
node3-1      | 2024-09-11 17:19:23,989|INFO|node_reg_handler.py|Loaded current node registry from the ledger: ['Node1', 'Node2', 'Node3', 'Node4']
node3-1      | 2024-09-11 17:19:23,989|INFO|node_reg_handler.py|Current committed node registry for previous views: [(0, ['Node1', 'Node2', 'Node3', 'Node4'])]
node3-1      | 2024-09-11 17:19:23,989|INFO|node_reg_handler.py|Current uncommitted node registry for previous views: [(0, ['Node1', 'Node2', 'Node3', 'Node4'])]
node4-1      | 2024-09-11 17:19:23,989|INFO|cons_proof_service.py|Node4:ConsProofService:0 finished with consistency proof None
node3-1      | 2024-09-11 17:19:23,989|INFO|node_reg_handler.py|Current active node registry: ['Node1', 'Node2', 'Node3', 'Node4']
node4-1      | 2024-09-11 17:19:23,989|INFO|catchup_rep_service.py|Node4:CatchupRepService:0 started catching up with LedgerCatchupStart(ledger_id=0, catchup_till=None, nodes_ledger_sizes={})
node3-1      | 2024-09-11 17:19:23,989|INFO|checkpoint_service.py|Node3:0 - checkpoint_service set watermarks as 0 300
node4-1      | 2024-09-11 17:19:23,989|INFO|catchup_rep_service.py|CATCH-UP: Node4:CatchupRepService:0 completed catching up ledger 0, caught up 0 in total
node4-1      | 2024-09-11 17:19:23,989|INFO|node_leecher_service.py|Node4:NodeLeecherService transitioning from PreSyncingPool to SyncingAudit
node3-1      | 2024-09-11 17:19:23,989|INFO|ordering_service.py|Node3:0 cleaning up till (0, 0)
node4-1      | 2024-09-11 17:19:23,989|INFO|cons_proof_service.py|Node4:ConsProofService:3 starts
node3-1      | 2024-09-11 17:19:23,989|INFO|checkpoint_service.py|Node3:0 - checkpoint_service marked stable checkpoint 0
node3-1      | 2024-09-11 17:19:23,989|INFO|ordering_service.py|Node3:0 set last ordered as (0, 3)
node4-1      | 2024-09-11 17:19:23,990|INFO|cons_proof_service.py|Node4:ConsProofService:3 asking for ledger status of ledger 3
node3-1      | 2024-09-11 17:19:23,990|INFO|checkpoint_service.py|Node3:1 - checkpoint_service removing all received checkpoints
node3-1      | 2024-09-11 17:19:23,991|INFO|checkpoint_service.py|Node3:1 - checkpoint_service set watermarks as 0 9223372036854775807
node3-1      | 2024-09-11 17:19:23,991|INFO|node.py|CATCH-UP: Node3 caught up till (0, 3)
node3-1      | 2024-09-11 17:19:23,991|INFO|node.py|CATCH-UP: Node3 does not need any more catchups
node3-1      | 2024-09-11 17:19:23,991|INFO|replica.py|Node3:0 setting primaryName for view no 0 to: None
node3-1      | 2024-09-11 17:19:23,991|INFO|replica.py|Node3:1 setting primaryName for view no 0 to: None
node3-1      | 2024-09-11 17:19:23,991|INFO|node.py|Node3 updated its pool parameters: f 1, totalNodes 4, allNodeNames {'Node4', 'Node3', 'Node1', 'Node2'}, requiredNumberOfInstances 2, minimumNodes 3, quorums {'n': 4, 'f': 1, 'weak': Quorum(2), 'strong': Quorum(3), 'propagate': Quorum(2), 'prepare': Quorum(2), 'commit': Quorum(3), 'reply': Quorum(2), 'view_change': Quorum(3), 'election': Quorum(3), 'view_change_ack': Quorum(2), 'view_change_done': Quorum(3), 'same_consistency_proof': Quorum(2), 'consistency_proof': Quorum(2), 'ledger_status': Quorum(2), 'ledger_status_last_3PC': Quorum(2), 'checkpoint': Quorum(2), 'timestamp': Quorum(2), 'bls_signatures': Quorum(3), 'observer_data': Quorum(2), 'backup_instance_faulty': Quorum(2)}
node3-1      | 2024-09-11 17:19:23,991|INFO|consensus_shared_data.py|Node3:0 updated validators list to {'Node4', 'Node3', 'Node1', 'Node2'}
node3-1      | 2024-09-11 17:19:23,991|INFO|consensus_shared_data.py|Node3:1 updated validators list to {'Node4', 'Node3', 'Node1', 'Node2'}
node3-1      | 2024-09-11 17:19:23,991|INFO|replica.py|Node3:0 setting primaryName for view no 0 to: Node1:0
node3-1      | 2024-09-11 17:19:23,992|NOTIFICATION|primary_connection_monitor_service.py|Node3:0 restored connection to primary of master
node3-1      | 2024-09-11 17:19:23,992|NOTIFICATION|node.py|PRIMARY SELECTION:  selected primary Node1:0 for instance 0 (view 0)
node3-1      | 2024-09-11 17:19:23,992|INFO|replica.py|Node3:1 setting primaryName for view no 0 to: Node2:1
node3-1      | 2024-09-11 17:19:23,992|NOTIFICATION|node.py|PRIMARY SELECTION:  selected primary Node2:1 for instance 1 (view 0)
node3-1      | 2024-09-11 17:19:23,992|INFO|node.py|Node3 started participating
node3-1      | 2024-09-11 17:19:23,992|INFO|checkpoint_service.py|update_watermark_from_3pc to (0, 3)
node3-1      | 2024-09-11 17:19:23,992|INFO|checkpoint_service.py|Node3:0 - checkpoint_service set watermarks as 3 303
node3-1      | 2024-09-11 17:19:23,992|INFO|checkpoint_service.py|Node3:1 - checkpoint_service set watermarks as 0 9223372036854775807
node3-1      | 2024-09-11 17:19:23,992|INFO|last_sent_pp_store_helper.py|Node3 trying to restore lastPrePrepareSeqNo
node3-1      | 2024-09-11 17:19:23,992|INFO|last_sent_pp_store_helper.py|Node3 did not find stored lastSentPrePrepare
node3-1      | 2024-09-11 17:19:23,992|INFO|last_sent_pp_store_helper.py|Node3 erasing stored lastSentPrePrepare
node3-1      | 2024-09-11 17:19:23,993|INFO|zstack.py|Processing messages from previously unknown remotes.
node3-1      | 2024-09-11 17:19:23,993|INFO|seeder_service.py|Node3 received ledger status: LEDGER_STATUS{'ledgerId': 0, 'txnSeqNo': 4, 'viewNo': None, 'ppSeqNo': None, 'merkleRoot': 'Cv3r9P26vvuKDekhaHSSUW1mBRihUSgTZcAzhmgAMa1A', 'protocolVersion': 2} from Node4
node3-1      | 2024-09-11 17:19:23,993|INFO|cons_proof_service.py|Node3:ConsProofService:0 ignoring LEDGER_STATUS{'ledgerId': 0, 'txnSeqNo': 4, 'viewNo': None, 'ppSeqNo': None, 'merkleRoot': 'Cv3r9P26vvuKDekhaHSSUW1mBRihUSgTZcAzhmgAMa1A', 'protocolVersion': 2} since it is not gathering ledger statuses
node3-1      | 2024-09-11 17:19:23,994|INFO|seeder_service.py|Node3 received ledger status: LEDGER_STATUS{'ledgerId': 3, 'txnSeqNo': 3, 'viewNo': None, 'ppSeqNo': None, 'merkleRoot': 'Hz5MC1sTjUFSgHaefctzCah7g752HmDqrN816PtC6tJD', 'protocolVersion': 2} from Node4
node3-1      | 2024-09-11 17:19:23,994|INFO|cons_proof_service.py|Node3:ConsProofService:3 ignoring LEDGER_STATUS{'ledgerId': 3, 'txnSeqNo': 3, 'viewNo': None, 'ppSeqNo': None, 'merkleRoot': 'Hz5MC1sTjUFSgHaefctzCah7g752HmDqrN816PtC6tJD', 'protocolVersion': 2} since it is not gathering ledger statuses
node3-1      | 2024-09-11 17:19:23,994|NOTIFICATION|keep_in_touch.py|Node3's connections changed from {'Node1', 'Node2'} to {'Node4', 'Node1', 'Node2'}
node3-1      | 2024-09-11 17:19:23,995|NOTIFICATION|keep_in_touch.py|CONNECTION: Node3 now connected to Node4
node3-1      | 2024-09-11 17:19:23,995|INFO|motor.py|Node3 changing status from started_hungry to started
node2-1      | 2024-09-11 17:19:23,998|INFO|seeder_service.py|Node2 received ledger status: LEDGER_STATUS{'ledgerId': 3, 'txnSeqNo': 3, 'viewNo': None, 'ppSeqNo': None, 'merkleRoot': 'Hz5MC1sTjUFSgHaefctzCah7g752HmDqrN816PtC6tJD', 'protocolVersion': 2} from Node4
node2-1      | 2024-09-11 17:19:23,998|INFO|cons_proof_service.py|Node2:ConsProofService:3 comparing its ledger 3 of size 3 with 3
node2-1      | 2024-09-11 17:19:23,998|INFO|cons_proof_service.py|Node2:ConsProofService:3 comparing its ledger 3 of size 3 with 3
node2-1      | 2024-09-11 17:19:23,999|INFO|seeder_service.py|Node2 received ledger status: LEDGER_STATUS{'ledgerId': 3, 'txnSeqNo': 3, 'viewNo': None, 'ppSeqNo': None, 'merkleRoot': 'Hz5MC1sTjUFSgHaefctzCah7g752HmDqrN816PtC6tJD', 'protocolVersion': 2} from Node1
node2-1      | 2024-09-11 17:19:23,999|INFO|cons_proof_service.py|Node2:ConsProofService:3 comparing its ledger 3 of size 3 with 3
node2-1      | 2024-09-11 17:19:23,999|INFO|cons_proof_service.py|Node2:ConsProofService:3 comparing its ledger 3 of size 3 with 3
node2-1      | 2024-09-11 17:19:23,999|INFO|cons_proof_service.py|Node2:ConsProofService:3 finished with consistency proof None
node2-1      | 2024-09-11 17:19:23,999|INFO|catchup_rep_service.py|Node2:CatchupRepService:3 started catching up with LedgerCatchupStart(ledger_id=3, catchup_till=None, nodes_ledger_sizes={})
node2-1      | 2024-09-11 17:19:23,999|INFO|catchup_rep_service.py|CATCH-UP: Node2:CatchupRepService:3 completed catching up ledger 3, caught up 0 in total
node2-1      | 2024-09-11 17:19:23,999|INFO|node_leecher_service.py|Node2:NodeLeecherService transitioning from SyncingAudit to SyncingPool
node2-1      | 2024-09-11 17:19:23,999|INFO|catchup_rep_service.py|Node2:CatchupRepService:0 started catching up with LedgerCatchupStart(ledger_id=0, catchup_till=None, nodes_ledger_sizes={})
node2-1      | 2024-09-11 17:19:24,000|INFO|catchup_rep_service.py|CATCH-UP: Node2:CatchupRepService:0 completed catching up ledger 0, caught up 0 in total
node2-1      | 2024-09-11 17:19:24,000|INFO|node_leecher_service.py|Node2:NodeLeecherService transitioning from SyncingPool to SyncingConfig
node2-1      | 2024-09-11 17:19:24,000|INFO|catchup_rep_service.py|Node2:CatchupRepService:2 started catching up with LedgerCatchupStart(ledger_id=2, catchup_till=None, nodes_ledger_sizes={})
node2-1      | 2024-09-11 17:19:24,000|INFO|catchup_rep_service.py|CATCH-UP: Node2:CatchupRepService:2 completed catching up ledger 2, caught up 0 in total
node2-1      | 2024-09-11 17:19:24,000|INFO|node_leecher_service.py|Node2:NodeLeecherService transitioning from SyncingConfig to SyncingOthers
node2-1      | 2024-09-11 17:19:24,000|INFO|catchup_rep_service.py|Node2:CatchupRepService:1 started catching up with LedgerCatchupStart(ledger_id=1, catchup_till=None, nodes_ledger_sizes={})
node2-1      | 2024-09-11 17:19:24,000|INFO|catchup_rep_service.py|CATCH-UP: Node2:CatchupRepService:1 completed catching up ledger 1, caught up 0 in total
node2-1      | 2024-09-11 17:19:24,000|INFO|node_leecher_service.py|Node2:NodeLeecherService transitioning from SyncingOthers to Idle
node2-1      | 2024-09-11 17:19:24,000|INFO|node.py|Node2 caught up to 0 txns in the last catchup
node2-1      | 2024-09-11 17:19:24,001|INFO|node_reg_handler.py|Loaded current node registry from the ledger: ['Node1', 'Node2', 'Node3', 'Node4']
node2-1      | 2024-09-11 17:19:24,001|INFO|node_reg_handler.py|Current committed node registry for previous views: [(0, ['Node1', 'Node2', 'Node3', 'Node4'])]
node2-1      | 2024-09-11 17:19:24,001|INFO|node_reg_handler.py|Current uncommitted node registry for previous views: [(0, ['Node1', 'Node2', 'Node3', 'Node4'])]
node2-1      | 2024-09-11 17:19:24,001|INFO|node_reg_handler.py|Current active node registry: ['Node1', 'Node2', 'Node3', 'Node4']
node2-1      | 2024-09-11 17:19:24,001|INFO|checkpoint_service.py|Node2:0 - checkpoint_service set watermarks as 0 300
node2-1      | 2024-09-11 17:19:24,001|INFO|ordering_service.py|Node2:0 cleaning up till (0, 0)
node2-1      | 2024-09-11 17:19:24,001|INFO|checkpoint_service.py|Node2:0 - checkpoint_service marked stable checkpoint 0
node2-1      | 2024-09-11 17:19:24,002|INFO|ordering_service.py|Node2:0 set last ordered as (0, 3)
node2-1      | 2024-09-11 17:19:24,002|INFO|node.py|CATCH-UP: Node2 caught up till (0, 3)
node2-1      | 2024-09-11 17:19:24,002|INFO|node.py|CATCH-UP: Node2 does not need any more catchups
node2-1      | 2024-09-11 17:19:24,003|INFO|replica.py|Node2:0 setting primaryName for view no 0 to: None
node2-1      | 2024-09-11 17:19:24,003|INFO|replica.py|Node2:1 setting primaryName for view no 0 to: None
node2-1      | 2024-09-11 17:19:24,003|INFO|node.py|Node2 updated its pool parameters: f 1, totalNodes 4, allNodeNames {'Node3', 'Node4', 'Node2', 'Node1'}, requiredNumberOfInstances 2, minimumNodes 3, quorums {'n': 4, 'f': 1, 'weak': Quorum(2), 'strong': Quorum(3), 'propagate': Quorum(2), 'prepare': Quorum(2), 'commit': Quorum(3), 'reply': Quorum(2), 'view_change': Quorum(3), 'election': Quorum(3), 'view_change_ack': Quorum(2), 'view_change_done': Quorum(3), 'same_consistency_proof': Quorum(2), 'consistency_proof': Quorum(2), 'ledger_status': Quorum(2), 'ledger_status_last_3PC': Quorum(2), 'checkpoint': Quorum(2), 'timestamp': Quorum(2), 'bls_signatures': Quorum(3), 'observer_data': Quorum(2), 'backup_instance_faulty': Quorum(2)}
node2-1      | 2024-09-11 17:19:24,003|INFO|consensus_shared_data.py|Node2:0 updated validators list to {'Node3', 'Node4', 'Node2', 'Node1'}
node2-1      | 2024-09-11 17:19:24,003|INFO|consensus_shared_data.py|Node2:1 updated validators list to {'Node3', 'Node4', 'Node2', 'Node1'}
node2-1      | 2024-09-11 17:19:24,003|INFO|replica.py|Node2:0 setting primaryName for view no 0 to: Node1:0
node2-1      | 2024-09-11 17:19:24,003|NOTIFICATION|primary_connection_monitor_service.py|Node2:0 restored connection to primary of master
node2-1      | 2024-09-11 17:19:24,003|NOTIFICATION|node.py|PRIMARY SELECTION:  selected primary Node1:0 for instance 0 (view 0)
node2-1      | 2024-09-11 17:19:24,003|INFO|replica.py|Node2:1 setting primaryName for view no 0 to: Node2:1
node2-1      | 2024-09-11 17:19:24,003|NOTIFICATION|node.py|PRIMARY SELECTION:  selected primary Node2:1 for instance 1 (view 0)
node4-1      | 2024-09-11 17:19:24,003|INFO|seeder_service.py|Node4 received ledger status: LEDGER_STATUS{'ledgerId': 3, 'txnSeqNo': 3, 'viewNo': None, 'ppSeqNo': None, 'merkleRoot': 'Hz5MC1sTjUFSgHaefctzCah7g752HmDqrN816PtC6tJD', 'protocolVersion': 2} from Node1
node4-1      | 2024-09-11 17:19:24,003|INFO|cons_proof_service.py|Node4:ConsProofService:3 comparing its ledger 3 of size 3 with 3
node2-1      | 2024-09-11 17:19:24,003|INFO|node.py|Node2 started participating
node2-1      | 2024-09-11 17:19:24,003|INFO|checkpoint_service.py|update_watermark_from_3pc to (0, 3)
node2-1      | 2024-09-11 17:19:24,003|INFO|checkpoint_service.py|Node2:0 - checkpoint_service set watermarks as 3 303
node4-1      | 2024-09-11 17:19:24,004|INFO|cons_proof_service.py|Node4:ConsProofService:3 comparing its ledger 3 of size 3 with 3
node2-1      | 2024-09-11 17:19:24,004|INFO|last_sent_pp_store_helper.py|Node2 trying to restore lastPrePrepareSeqNo
node2-1      | 2024-09-11 17:19:24,004|INFO|last_sent_pp_store_helper.py|Node2 did not find stored lastSentPrePrepare
node2-1      | 2024-09-11 17:19:24,004|INFO|last_sent_pp_store_helper.py|Node2 erasing stored lastSentPrePrepare
node4-1      | 2024-09-11 17:19:24,004|INFO|seeder_service.py|Node4 received ledger status: LEDGER_STATUS{'ledgerId': 0, 'txnSeqNo': 4, 'viewNo': None, 'ppSeqNo': None, 'merkleRoot': 'Cv3r9P26vvuKDekhaHSSUW1mBRihUSgTZcAzhmgAMa1A', 'protocolVersion': 2} from Node3
node4-1      | 2024-09-11 17:19:24,004|INFO|cons_proof_service.py|Node4:ConsProofService:0 ignoring LEDGER_STATUS{'ledgerId': 0, 'txnSeqNo': 4, 'viewNo': None, 'ppSeqNo': None, 'merkleRoot': 'Cv3r9P26vvuKDekhaHSSUW1mBRihUSgTZcAzhmgAMa1A', 'protocolVersion': 2} since it is not gathering ledger statuses
node2-1      | 2024-09-11 17:19:24,004|INFO|zstack.py|Processing messages from previously unknown remotes.
node2-1      | 2024-09-11 17:19:24,004|INFO|seeder_service.py|Node2 received ledger status: LEDGER_STATUS{'ledgerId': 3, 'txnSeqNo': 3, 'viewNo': None, 'ppSeqNo': None, 'merkleRoot': 'Hz5MC1sTjUFSgHaefctzCah7g752HmDqrN816PtC6tJD', 'protocolVersion': 2} from Node3
node2-1      | 2024-09-11 17:19:24,005|INFO|cons_proof_service.py|Node2:ConsProofService:3 ignoring LEDGER_STATUS{'ledgerId': 3, 'txnSeqNo': 3, 'viewNo': None, 'ppSeqNo': None, 'merkleRoot': 'Hz5MC1sTjUFSgHaefctzCah7g752HmDqrN816PtC6tJD', 'protocolVersion': 2} since it is not gathering ledger statuses
node4-1      | 2024-09-11 17:19:24,004|INFO|seeder_service.py|Node4 received ledger status: LEDGER_STATUS{'ledgerId': 3, 'txnSeqNo': 3, 'viewNo': None, 'ppSeqNo': None, 'merkleRoot': 'Hz5MC1sTjUFSgHaefctzCah7g752HmDqrN816PtC6tJD', 'protocolVersion': 2} from Node3
node4-1      | 2024-09-11 17:19:24,004|INFO|cons_proof_service.py|Node4:ConsProofService:3 comparing its ledger 3 of size 3 with 3
node4-1      | 2024-09-11 17:19:24,004|INFO|cons_proof_service.py|Node4:ConsProofService:3 comparing its ledger 3 of size 3 with 3
node4-1      | 2024-09-11 17:19:24,004|INFO|cons_proof_service.py|Node4:ConsProofService:3 finished with consistency proof None
node4-1      | 2024-09-11 17:19:24,004|INFO|catchup_rep_service.py|Node4:CatchupRepService:3 started catching up with LedgerCatchupStart(ledger_id=3, catchup_till=None, nodes_ledger_sizes={})
node4-1      | 2024-09-11 17:19:24,005|INFO|catchup_rep_service.py|CATCH-UP: Node4:CatchupRepService:3 completed catching up ledger 3, caught up 0 in total
node4-1      | 2024-09-11 17:19:24,005|INFO|node_leecher_service.py|Node4:NodeLeecherService transitioning from SyncingAudit to SyncingPool
node4-1      | 2024-09-11 17:19:24,005|INFO|catchup_rep_service.py|Node4:CatchupRepService:0 started catching up with LedgerCatchupStart(ledger_id=0, catchup_till=None, nodes_ledger_sizes={})
node4-1      | 2024-09-11 17:19:24,005|INFO|catchup_rep_service.py|CATCH-UP: Node4:CatchupRepService:0 completed catching up ledger 0, caught up 0 in total
node4-1      | 2024-09-11 17:19:24,005|INFO|node_leecher_service.py|Node4:NodeLeecherService transitioning from SyncingPool to SyncingConfig
node4-1      | 2024-09-11 17:19:24,005|INFO|catchup_rep_service.py|Node4:CatchupRepService:2 started catching up with LedgerCatchupStart(ledger_id=2, catchup_till=None, nodes_ledger_sizes={})
node4-1      | 2024-09-11 17:19:24,005|INFO|catchup_rep_service.py|CATCH-UP: Node4:CatchupRepService:2 completed catching up ledger 2, caught up 0 in total
node4-1      | 2024-09-11 17:19:24,005|INFO|node_leecher_service.py|Node4:NodeLeecherService transitioning from SyncingConfig to SyncingOthers
node4-1      | 2024-09-11 17:19:24,005|INFO|catchup_rep_service.py|Node4:CatchupRepService:1 started catching up with LedgerCatchupStart(ledger_id=1, catchup_till=None, nodes_ledger_sizes={})
node4-1      | 2024-09-11 17:19:24,006|INFO|catchup_rep_service.py|CATCH-UP: Node4:CatchupRepService:1 completed catching up ledger 1, caught up 0 in total
node4-1      | 2024-09-11 17:19:24,006|INFO|node_leecher_service.py|Node4:NodeLeecherService transitioning from SyncingOthers to Idle
node4-1      | 2024-09-11 17:19:24,006|INFO|node.py|Node4 caught up to 0 txns in the last catchup
node4-1      | 2024-09-11 17:19:24,006|INFO|node_reg_handler.py|Loaded current node registry from the ledger: ['Node1', 'Node2', 'Node3', 'Node4']
node4-1      | 2024-09-11 17:19:24,006|INFO|node_reg_handler.py|Current committed node registry for previous views: [(0, ['Node1', 'Node2', 'Node3', 'Node4'])]
node4-1      | 2024-09-11 17:19:24,006|INFO|node_reg_handler.py|Current uncommitted node registry for previous views: [(0, ['Node1', 'Node2', 'Node3', 'Node4'])]
node4-1      | 2024-09-11 17:19:24,006|INFO|node_reg_handler.py|Current active node registry: ['Node1', 'Node2', 'Node3', 'Node4']
node4-1      | 2024-09-11 17:19:24,007|INFO|checkpoint_service.py|Node4:0 - checkpoint_service set watermarks as 0 300
node4-1      | 2024-09-11 17:19:24,007|INFO|ordering_service.py|Node4:0 cleaning up till (0, 0)
node4-1      | 2024-09-11 17:19:24,007|INFO|checkpoint_service.py|Node4:0 - checkpoint_service marked stable checkpoint 0
node4-1      | 2024-09-11 17:19:24,007|INFO|ordering_service.py|Node4:0 set last ordered as (0, 3)
node4-1      | 2024-09-11 17:19:24,008|INFO|checkpoint_service.py|Node4:1 - checkpoint_service removing all received checkpoints
node4-1      | 2024-09-11 17:19:24,008|INFO|checkpoint_service.py|Node4:1 - checkpoint_service set watermarks as 0 9223372036854775807
node4-1      | 2024-09-11 17:19:24,008|INFO|node.py|CATCH-UP: Node4 caught up till (0, 3)
node4-1      | 2024-09-11 17:19:24,008|INFO|node.py|CATCH-UP: Node4 does not need any more catchups
node4-1      | 2024-09-11 17:19:24,008|INFO|replica.py|Node4:0 setting primaryName for view no 0 to: None
node4-1      | 2024-09-11 17:19:24,008|INFO|replica.py|Node4:1 setting primaryName for view no 0 to: None
node4-1      | 2024-09-11 17:19:24,009|INFO|node.py|Node4 updated its pool parameters: f 1, totalNodes 4, allNodeNames {'Node3', 'Node2', 'Node4', 'Node1'}, requiredNumberOfInstances 2, minimumNodes 3, quorums {'n': 4, 'f': 1, 'weak': Quorum(2), 'strong': Quorum(3), 'propagate': Quorum(2), 'prepare': Quorum(2), 'commit': Quorum(3), 'reply': Quorum(2), 'view_change': Quorum(3), 'election': Quorum(3), 'view_change_ack': Quorum(2), 'view_change_done': Quorum(3), 'same_consistency_proof': Quorum(2), 'consistency_proof': Quorum(2), 'ledger_status': Quorum(2), 'ledger_status_last_3PC': Quorum(2), 'checkpoint': Quorum(2), 'timestamp': Quorum(2), 'bls_signatures': Quorum(3), 'observer_data': Quorum(2), 'backup_instance_faulty': Quorum(2)}
node4-1      | 2024-09-11 17:19:24,009|INFO|consensus_shared_data.py|Node4:0 updated validators list to {'Node3', 'Node2', 'Node4', 'Node1'}
node4-1      | 2024-09-11 17:19:24,009|INFO|consensus_shared_data.py|Node4:1 updated validators list to {'Node3', 'Node2', 'Node4', 'Node1'}
node4-1      | 2024-09-11 17:19:24,009|INFO|replica.py|Node4:0 setting primaryName for view no 0 to: Node1:0
node4-1      | 2024-09-11 17:19:24,009|NOTIFICATION|primary_connection_monitor_service.py|Node4:0 restored connection to primary of master
node4-1      | 2024-09-11 17:19:24,009|NOTIFICATION|node.py|PRIMARY SELECTION:  selected primary Node1:0 for instance 0 (view 0)
node4-1      | 2024-09-11 17:19:24,009|INFO|replica.py|Node4:1 setting primaryName for view no 0 to: Node2:1
node4-1      | 2024-09-11 17:19:24,009|NOTIFICATION|node.py|PRIMARY SELECTION:  selected primary Node2:1 for instance 1 (view 0)
node4-1      | 2024-09-11 17:19:24,009|INFO|node.py|Node4 started participating
node4-1      | 2024-09-11 17:19:24,010|INFO|checkpoint_service.py|update_watermark_from_3pc to (0, 3)
node4-1      | 2024-09-11 17:19:24,010|INFO|checkpoint_service.py|Node4:0 - checkpoint_service set watermarks as 3 303
node4-1      | 2024-09-11 17:19:24,010|INFO|checkpoint_service.py|Node4:1 - checkpoint_service set watermarks as 0 9223372036854775807
node4-1      | 2024-09-11 17:19:24,010|INFO|last_sent_pp_store_helper.py|Node4 trying to restore lastPrePrepareSeqNo
node4-1      | 2024-09-11 17:19:24,010|INFO|last_sent_pp_store_helper.py|Node4 did not find stored lastSentPrePrepare
node4-1      | 2024-09-11 17:19:24,010|INFO|last_sent_pp_store_helper.py|Node4 erasing stored lastSentPrePrepare
node4-1      | 2024-09-11 17:19:24,010|INFO|zstack.py|Processing messages from previously unknown remotes.
node4-1      | 2024-09-11 17:19:24,012|INFO|seeder_service.py|Node4 received ledger status: LEDGER_STATUS{'ledgerId': 3, 'txnSeqNo': 3, 'viewNo': None, 'ppSeqNo': None, 'merkleRoot': 'Hz5MC1sTjUFSgHaefctzCah7g752HmDqrN816PtC6tJD', 'protocolVersion': 2} from Node2
node4-1      | 2024-09-11 17:19:24,012|INFO|cons_proof_service.py|Node4:ConsProofService:3 ignoring LEDGER_STATUS{'ledgerId': 3, 'txnSeqNo': 3, 'viewNo': None, 'ppSeqNo': None, 'merkleRoot': 'Hz5MC1sTjUFSgHaefctzCah7g752HmDqrN816PtC6tJD', 'protocolVersion': 2} since it is not gathering ledger statuses
webserver-1  | INFO:__main__:REGISTER_NEW_DIDS is set to True
webserver-1  | INFO:__main__:LEDGER_INSTANCE_NAME is set to "localhost"
webserver-1  | INFO:__main__:Web analytics are DISABLED
webserver-1  | INFO:__main__:Running webserver...
webserver-1  | INFO:__main__:Creating trust anchor...
webserver-1  | INFO:server.anchor:Ledger cache will be stored in :memory:
webserver-1  | ======== Running on http://0.0.0.0:8000 ========
webserver-1  | (Press CTRL+C to quit)
webserver-1  | INFO:server.anchor:Initializing transaction database
webserver-1  | INFO:server.anchor:Genesis file found: /home/indy/ledger/sandbox/pool_transactions_genesis
webserver-1  | INFO:server.anchor:Connecting to ledger pool
node1-1      | 2024-09-11 17:19:29,507|INFO|seeder_service.py|Node1 received ledger status: LEDGER_STATUS{'ledgerId': 0, 'txnSeqNo': 4, 'viewNo': None, 'ppSeqNo': None, 'merkleRoot': 'Cv3r9P26vvuKDekhaHSSUW1mBRihUSgTZcAzhmgAMa1A', 'protocolVersion': 2} from b'hRrm29b2IHEUuX76f72zy56CIuZXu4fcccjtGeb8sCY='
node4-1      | 2024-09-11 17:19:29,508|INFO|seeder_service.py|Node4 received ledger status: LEDGER_STATUS{'ledgerId': 0, 'txnSeqNo': 4, 'viewNo': None, 'ppSeqNo': None, 'merkleRoot': 'Cv3r9P26vvuKDekhaHSSUW1mBRihUSgTZcAzhmgAMa1A', 'protocolVersion': 2} from b'hRrm29b2IHEUuX76f72zy56CIuZXu4fcccjtGeb8sCY='
node2-1      | 2024-09-11 17:19:29,509|INFO|seeder_service.py|Node2 received ledger status: LEDGER_STATUS{'ledgerId': 0, 'txnSeqNo': 4, 'viewNo': None, 'ppSeqNo': None, 'merkleRoot': 'Cv3r9P26vvuKDekhaHSSUW1mBRihUSgTZcAzhmgAMa1A', 'protocolVersion': 2} from b'hRrm29b2IHEUuX76f72zy56CIuZXu4fcccjtGeb8sCY='
webserver-1  | INFO:server.anchor:Finished pool refresh: {'mt_root': 'Cv3r9P26vvuKDekhaHSSUW1mBRihUSgTZcAzhmgAMa1A', 'mt_size': 4, 'nodes': ['Node4', 'Node3', 'Node2', 'Node1']}
node3-1      | 2024-09-11 17:19:29,517|INFO|seeder_service.py|Node3 received ledger status: LEDGER_STATUS{'ledgerId': 0, 'txnSeqNo': 4, 'viewNo': None, 'ppSeqNo': None, 'merkleRoot': 'Cv3r9P26vvuKDekhaHSSUW1mBRihUSgTZcAzhmgAMa1A', 'protocolVersion': 2} from b'hRrm29b2IHEUuX76f72zy56CIuZXu4fcccjtGeb8sCY='
webserver-1  | INFO:server.anchor:No AML defined
webserver-1  | INFO:server.anchor:No TAA defined
webserver-1  | INFO:server.anchor:Init ledger cache...
webserver-1  | INFO:__main__:--- Trust anchor initialized ---
webserver-1  | INFO:server.anchor:POOL ledger synced with 4 transaction(s)
webserver-1  | INFO:server.anchor:DOMAIN ledger synced with 5 transaction(s)
webserver-1  | INFO:server.anchor:CONFIG ledger synced with 0 transaction(s)
webserver-1  | INFO:server.anchor:Finished cache init
node1-1      | 2024-09-11 17:20:23,918|INFO|primary_connection_monitor_service.py|Node1:1 The primary is already connected so view change will not be proposed
node4-1      | 2024-09-11 17:20:23,929|INFO|primary_connection_monitor_service.py|Node4:1 The primary is already connected so view change will not be proposed
node3-1      | 2024-09-11 17:20:23,953|INFO|primary_connection_monitor_service.py|Node3:1 The primary is already connected so view change will not be proposed
webserver-1  | INFO:aiohttp.access:192.168.65.1 [11/Sep/2024:17:20:28 +0000] "GET /genesis HTTP/1.1" 200 3308 "-" "Python/3.12 aiohttp/3.10.5"
webserver-1  | INFO:server.anchor:Register agent
webserver-1  | INFO:server.anchor:Get nym: VX3a3ZJ5tqrp33QKRGv8N4
webserver-1  | INFO:server.anchor:Send nym: VX3a3ZJ5tqrp33QKRGv8N4/GYWbseGp7EFBqVMoboB65U5g7AEsU9J7qSNLXaLJvdPY
node2-1      | 2024-09-11 17:20:28,093|INFO|last_sent_pp_store_helper.py|Node2 did not find stored lastSentPrePrepare
node3-1      | 2024-09-11 17:20:28,101|INFO|last_sent_pp_store_helper.py|Node3 did not find stored lastSentPrePrepare
node1-1      | 2024-09-11 17:20:28,107|INFO|last_sent_pp_store_helper.py|Node1 did not find stored lastSentPrePrepare
node4-1      | 2024-09-11 17:20:28,109|INFO|last_sent_pp_store_helper.py|Node4 did not find stored lastSentPrePrepare
node2-1      | 2024-09-11 17:20:28,118|INFO|ordering_service.py|Node2:1 set last ordered as (0, 1)
node2-1      | 2024-09-11 17:20:28,119|INFO|ordering_service.py|Node2:1 ordered batch request, view no 0, ppSeqNo 1, ledger 1, state root None, txn root None, audit root None, requests ordered 1, discarded 0
node3-1      | 2024-09-11 17:20:28,123|INFO|ordering_service.py|Node3:1 set last ordered as (0, 1)
node3-1      | 2024-09-11 17:20:28,124|INFO|ordering_service.py|Node3:1 ordered batch request, view no 0, ppSeqNo 1, ledger 1, state root None, txn root None, audit root None, requests ordered 1, discarded 0
node4-1      | 2024-09-11 17:20:28,125|INFO|ordering_service.py|Node4:1 set last ordered as (0, 1)
node4-1      | 2024-09-11 17:20:28,126|INFO|ordering_service.py|Node4:1 ordered batch request, view no 0, ppSeqNo 1, ledger 1, state root None, txn root None, audit root None, requests ordered 1, discarded 0
node1-1      | 2024-09-11 17:20:28,128|INFO|ordering_service.py|Node1:1 set last ordered as (0, 1)
node1-1      | 2024-09-11 17:20:28,129|INFO|ordering_service.py|Node1:1 ordered batch request, view no 0, ppSeqNo 1, ledger 1, state root None, txn root None, audit root None, requests ordered 1, discarded 0
node1-1      | 2024-09-11 17:20:28,139|INFO|ordering_service.py|Node1:0 set last ordered as (0, 4)
node3-1      | 2024-09-11 17:20:28,141|INFO|ordering_service.py|Node3:0 set last ordered as (0, 4)
node1-1      | 2024-09-11 17:20:28,145|INFO|ordering_service.py|Node1:0 ordered batch request, view no 0, ppSeqNo 4, ledger 1, state root HaX66bTixVBAd9PGydtDwFJn38qbJ2htzaFg33PGCFWC, txn root FqWQr5WtR9B9xaaiLN3hwmKe8Uoq8NXG71R2xsXtwudV, audit root 3Gwnx45yLyJYeQkJTkDaiqtnuJABfnStnYXXiJUqEeqc, requests ordered 1, discarded 0
node2-1      | 2024-09-11 17:20:28,145|INFO|ordering_service.py|Node2:0 set last ordered as (0, 4)
node3-1      | 2024-09-11 17:20:28,147|INFO|ordering_service.py|Node3:0 ordered batch request, view no 0, ppSeqNo 4, ledger 1, state root HaX66bTixVBAd9PGydtDwFJn38qbJ2htzaFg33PGCFWC, txn root FqWQr5WtR9B9xaaiLN3hwmKe8Uoq8NXG71R2xsXtwudV, audit root 3Gwnx45yLyJYeQkJTkDaiqtnuJABfnStnYXXiJUqEeqc, requests ordered 1, discarded 0
webserver-1  | INFO:aiohttp.access:192.168.65.1 [11/Sep/2024:17:20:28 +0000] "POST /register HTTP/1.1" 200 333 "-" "Python/3.12 aiohttp/3.10.5"
node4-1      | 2024-09-11 17:20:28,148|INFO|ordering_service.py|Node4:0 set last ordered as (0, 4)
node2-1      | 2024-09-11 17:20:28,151|INFO|ordering_service.py|Node2:0 ordered batch request, view no 0, ppSeqNo 4, ledger 1, state root HaX66bTixVBAd9PGydtDwFJn38qbJ2htzaFg33PGCFWC, txn root FqWQr5WtR9B9xaaiLN3hwmKe8Uoq8NXG71R2xsXtwudV, audit root 3Gwnx45yLyJYeQkJTkDaiqtnuJABfnStnYXXiJUqEeqc, requests ordered 1, discarded 0
node4-1      | 2024-09-11 17:20:28,154|INFO|ordering_service.py|Node4:0 ordered batch request, view no 0, ppSeqNo 4, ledger 1, state root HaX66bTixVBAd9PGydtDwFJn38qbJ2htzaFg33PGCFWC, txn root FqWQr5WtR9B9xaaiLN3hwmKe8Uoq8NXG71R2xsXtwudV, audit root 3Gwnx45yLyJYeQkJTkDaiqtnuJABfnStnYXXiJUqEeqc, requests ordered 1, discarded 0
node2-1      | 2024-09-11 17:20:30,452|INFO|seeder_service.py|Node2 received ledger status: LEDGER_STATUS{'ledgerId': 0, 'txnSeqNo': 4, 'viewNo': None, 'ppSeqNo': None, 'merkleRoot': 'Cv3r9P26vvuKDekhaHSSUW1mBRihUSgTZcAzhmgAMa1A', 'protocolVersion': 2} from b'l/Z6qTfr8AljzIUbImw5LaeKfmBnOUSIHRKKkTpme3U='
node4-1      | 2024-09-11 17:20:30,461|INFO|seeder_service.py|Node4 received ledger status: LEDGER_STATUS{'ledgerId': 0, 'txnSeqNo': 4, 'viewNo': None, 'ppSeqNo': None, 'merkleRoot': 'Cv3r9P26vvuKDekhaHSSUW1mBRihUSgTZcAzhmgAMa1A', 'protocolVersion': 2} from b'l/Z6qTfr8AljzIUbImw5LaeKfmBnOUSIHRKKkTpme3U='
node3-1      | 2024-09-11 17:20:30,462|INFO|seeder_service.py|Node3 received ledger status: LEDGER_STATUS{'ledgerId': 0, 'txnSeqNo': 4, 'viewNo': None, 'ppSeqNo': None, 'merkleRoot': 'Cv3r9P26vvuKDekhaHSSUW1mBRihUSgTZcAzhmgAMa1A', 'protocolVersion': 2} from b'l/Z6qTfr8AljzIUbImw5LaeKfmBnOUSIHRKKkTpme3U='
node1-1      | 2024-09-11 17:20:30,468|INFO|seeder_service.py|Node1 received ledger status: LEDGER_STATUS{'ledgerId': 0, 'txnSeqNo': 4, 'viewNo': None, 'ppSeqNo': None, 'merkleRoot': 'Cv3r9P26vvuKDekhaHSSUW1mBRihUSgTZcAzhmgAMa1A', 'protocolVersion': 2} from b'l/Z6qTfr8AljzIUbImw5LaeKfmBnOUSIHRKKkTpme3U='
node2-1      | 2024-09-11 17:20:31,128|INFO|ordering_service.py|Node2:1 set last ordered as (0, 2)
node3-1      | 2024-09-11 17:20:31,128|INFO|ordering_service.py|Node3:1 set last ordered as (0, 2)
node3-1      | 2024-09-11 17:20:31,128|INFO|ordering_service.py|Node3:1 ordered batch request, view no 0, ppSeqNo 2, ledger 1, state root None, txn root None, audit root None, requests ordered 1, discarded 0
node2-1      | 2024-09-11 17:20:31,128|INFO|ordering_service.py|Node2:1 ordered batch request, view no 0, ppSeqNo 2, ledger 1, state root None, txn root None, audit root None, requests ordered 1, discarded 0
node1-1      | 2024-09-11 17:20:31,131|INFO|ordering_service.py|Node1:1 set last ordered as (0, 2)
node4-1      | 2024-09-11 17:20:31,131|INFO|ordering_service.py|Node4:1 set last ordered as (0, 2)
node1-1      | 2024-09-11 17:20:31,131|INFO|ordering_service.py|Node1:1 ordered batch request, view no 0, ppSeqNo 2, ledger 1, state root None, txn root None, audit root None, requests ordered 1, discarded 0
node4-1      | 2024-09-11 17:20:31,131|INFO|ordering_service.py|Node4:1 ordered batch request, view no 0, ppSeqNo 2, ledger 1, state root None, txn root None, audit root None, requests ordered 1, discarded 0
node3-1      | 2024-09-11 17:20:31,136|INFO|ordering_service.py|Node3:0 set last ordered as (0, 5)
node2-1      | 2024-09-11 17:20:31,137|INFO|ordering_service.py|Node2:0 set last ordered as (0, 5)
node4-1      | 2024-09-11 17:20:31,137|INFO|ordering_service.py|Node4:0 set last ordered as (0, 5)
node1-1      | 2024-09-11 17:20:31,137|INFO|ordering_service.py|Node1:0 set last ordered as (0, 5)
node3-1      | 2024-09-11 17:20:31,139|INFO|ordering_service.py|Node3:0 ordered batch request, view no 0, ppSeqNo 5, ledger 1, state root FSGENJvYtpRo4BiJAVwcje8W5PXQfH3qgpDDPpAqDe3N, txn root 8gSM87DL8kC7oCHx8NkgJiSxDnu5rqHvSP4Tp8hj4wL9, audit root A517gXgtawY1K1gGDGLF6ZS8vbQj7VkXE74scSq2Epvm, requests ordered 1, discarded 0
node2-1      | 2024-09-11 17:20:31,140|INFO|ordering_service.py|Node2:0 ordered batch request, view no 0, ppSeqNo 5, ledger 1, state root FSGENJvYtpRo4BiJAVwcje8W5PXQfH3qgpDDPpAqDe3N, txn root 8gSM87DL8kC7oCHx8NkgJiSxDnu5rqHvSP4Tp8hj4wL9, audit root A517gXgtawY1K1gGDGLF6ZS8vbQj7VkXE74scSq2Epvm, requests ordered 1, discarded 0
node4-1      | 2024-09-11 17:20:31,140|INFO|ordering_service.py|Node4:0 ordered batch request, view no 0, ppSeqNo 5, ledger 1, state root FSGENJvYtpRo4BiJAVwcje8W5PXQfH3qgpDDPpAqDe3N, txn root 8gSM87DL8kC7oCHx8NkgJiSxDnu5rqHvSP4Tp8hj4wL9, audit root A517gXgtawY1K1gGDGLF6ZS8vbQj7VkXE74scSq2Epvm, requests ordered 1, discarded 0
node1-1      | 2024-09-11 17:20:31,141|INFO|ordering_service.py|Node1:0 ordered batch request, view no 0, ppSeqNo 5, ledger 1, state root FSGENJvYtpRo4BiJAVwcje8W5PXQfH3qgpDDPpAqDe3N, txn root 8gSM87DL8kC7oCHx8NkgJiSxDnu5rqHvSP4Tp8hj4wL9, audit root A517gXgtawY1K1gGDGLF6ZS8vbQj7VkXE74scSq2Epvm, requests ordered 1, discarded 0
webserver-1  | INFO:aiohttp.access:192.168.65.1 [11/Sep/2024:17:20:33 +0000] "GET /genesis HTTP/1.1" 200 3308 "-" "Python/3.12 aiohttp/3.10.5"
node1-1      | 2024-09-11 17:20:34,134|INFO|ordering_service.py|Node1:1 set last ordered as (0, 3)
node1-1      | 2024-09-11 17:20:34,134|INFO|ordering_service.py|Node1:1 ordered batch request, view no 0, ppSeqNo 3, ledger 1, state root None, txn root None, audit root None, requests ordered 1, discarded 0
node2-1      | 2024-09-11 17:20:34,135|INFO|ordering_service.py|Node2:1 set last ordered as (0, 3)
node2-1      | 2024-09-11 17:20:34,135|INFO|ordering_service.py|Node2:1 ordered batch request, view no 0, ppSeqNo 3, ledger 1, state root None, txn root None, audit root None, requests ordered 1, discarded 0
node1-1      | 2024-09-11 17:20:34,140|INFO|ordering_service.py|Node1:0 set last ordered as (0, 6)
node2-1      | 2024-09-11 17:20:34,140|INFO|ordering_service.py|Node2:0 set last ordered as (0, 6)
node4-1      | 2024-09-11 17:20:34,142|INFO|ordering_service.py|Node4:0 set last ordered as (0, 6)
node1-1      | 2024-09-11 17:20:34,143|INFO|ordering_service.py|Node1:0 ordered batch request, view no 0, ppSeqNo 6, ledger 1, state root 7HkM4DPEWXt1JaoPLsfCfimsxrdPKBCLpYN8av4uaiSU, txn root 6LDbLP5T26zm1YcSEMiAndz7D7wedegrLUxJzcJXu2pE, audit root A6axvJvbSGGbBEetjsryTd5muhBdPktyDbVLJ5dDagnk, requests ordered 1, discarded 0
node2-1      | 2024-09-11 17:20:34,143|INFO|ordering_service.py|Node2:0 ordered batch request, view no 0, ppSeqNo 6, ledger 1, state root 7HkM4DPEWXt1JaoPLsfCfimsxrdPKBCLpYN8av4uaiSU, txn root 6LDbLP5T26zm1YcSEMiAndz7D7wedegrLUxJzcJXu2pE, audit root A6axvJvbSGGbBEetjsryTd5muhBdPktyDbVLJ5dDagnk, requests ordered 1, discarded 0
node4-1      | 2024-09-11 17:20:34,146|INFO|ordering_service.py|Node4:0 ordered batch request, view no 0, ppSeqNo 6, ledger 1, state root 7HkM4DPEWXt1JaoPLsfCfimsxrdPKBCLpYN8av4uaiSU, txn root 6LDbLP5T26zm1YcSEMiAndz7D7wedegrLUxJzcJXu2pE, audit root A6axvJvbSGGbBEetjsryTd5muhBdPktyDbVLJ5dDagnk, requests ordered 1, discarded 0
node4-1      | 2024-09-11 17:20:34,146|INFO|ordering_service.py|Node4:1 set last ordered as (0, 3)
node4-1      | 2024-09-11 17:20:34,147|INFO|ordering_service.py|Node4:1 ordered batch request, view no 0, ppSeqNo 3, ledger 1, state root None, txn root None, audit root None, requests ordered 1, discarded 0
node3-1      | 2024-09-11 17:20:34,149|INFO|ordering_service.py|Node3:0 set last ordered as (0, 6)
node3-1      | 2024-09-11 17:20:34,152|INFO|ordering_service.py|Node3:0 ordered batch request, view no 0, ppSeqNo 6, ledger 1, state root 7HkM4DPEWXt1JaoPLsfCfimsxrdPKBCLpYN8av4uaiSU, txn root 6LDbLP5T26zm1YcSEMiAndz7D7wedegrLUxJzcJXu2pE, audit root A6axvJvbSGGbBEetjsryTd5muhBdPktyDbVLJ5dDagnk, requests ordered 1, discarded 0
node3-1      | 2024-09-11 17:20:34,153|INFO|ordering_service.py|Node3:1 set last ordered as (0, 3)
node3-1      | 2024-09-11 17:20:34,153|INFO|ordering_service.py|Node3:1 ordered batch request, view no 0, ppSeqNo 3, ledger 1, state root None, txn root None, audit root None, requests ordered 1, discarded 0
node3-1      | 2024-09-11 17:20:36,066|INFO|seeder_service.py|Node3 received ledger status: LEDGER_STATUS{'ledgerId': 0, 'txnSeqNo': 4, 'viewNo': None, 'ppSeqNo': None, 'merkleRoot': 'Cv3r9P26vvuKDekhaHSSUW1mBRihUSgTZcAzhmgAMa1A', 'protocolVersion': 2} from b'TmOEiRl0+eYDzbox6MGplLa50V3JWT4ZqZqSYAuyLmI='
node2-1      | 2024-09-11 17:20:36,072|INFO|seeder_service.py|Node2 received ledger status: LEDGER_STATUS{'ledgerId': 0, 'txnSeqNo': 4, 'viewNo': None, 'ppSeqNo': None, 'merkleRoot': 'Cv3r9P26vvuKDekhaHSSUW1mBRihUSgTZcAzhmgAMa1A', 'protocolVersion': 2} from b'TmOEiRl0+eYDzbox6MGplLa50V3JWT4ZqZqSYAuyLmI='
node1-1      | 2024-09-11 17:20:36,079|INFO|seeder_service.py|Node1 received ledger status: LEDGER_STATUS{'ledgerId': 0, 'txnSeqNo': 4, 'viewNo': None, 'ppSeqNo': None, 'merkleRoot': 'Cv3r9P26vvuKDekhaHSSUW1mBRihUSgTZcAzhmgAMa1A', 'protocolVersion': 2} from b'TmOEiRl0+eYDzbox6MGplLa50V3JWT4ZqZqSYAuyLmI='
node4-1      | 2024-09-11 17:20:36,080|INFO|seeder_service.py|Node4 received ledger status: LEDGER_STATUS{'ledgerId': 0, 'txnSeqNo': 4, 'viewNo': None, 'ppSeqNo': None, 'merkleRoot': 'Cv3r9P26vvuKDekhaHSSUW1mBRihUSgTZcAzhmgAMa1A', 'protocolVersion': 2} from b'TmOEiRl0+eYDzbox6MGplLa50V3JWT4ZqZqSYAuyLmI='
node4-1      | 2024-09-11 17:20:39,652|INFO|ordering_service.py|Node4:1 set last ordered as (0, 4)
node4-1      | 2024-09-11 17:20:39,652|INFO|ordering_service.py|Node4:1 ordered batch request, view no 0, ppSeqNo 4, ledger 1, state root None, txn root None, audit root None, requests ordered 1, discarded 0
node2-1      | 2024-09-11 17:20:39,655|INFO|ordering_service.py|Node2:1 set last ordered as (0, 4)
node2-1      | 2024-09-11 17:20:39,655|INFO|ordering_service.py|Node2:1 ordered batch request, view no 0, ppSeqNo 4, ledger 1, state root None, txn root None, audit root None, requests ordered 1, discarded 0
node1-1      | 2024-09-11 17:20:39,656|INFO|ordering_service.py|Node1:1 set last ordered as (0, 4)
node1-1      | 2024-09-11 17:20:39,656|INFO|ordering_service.py|Node1:1 ordered batch request, view no 0, ppSeqNo 4, ledger 1, state root None, txn root None, audit root None, requests ordered 1, discarded 0
node2-1      | 2024-09-11 17:20:39,661|INFO|ordering_service.py|Node2:0 set last ordered as (0, 7)
node1-1      | 2024-09-11 17:20:39,662|INFO|ordering_service.py|Node1:0 set last ordered as (0, 7)
node2-1      | 2024-09-11 17:20:39,664|INFO|ordering_service.py|Node2:0 ordered batch request, view no 0, ppSeqNo 7, ledger 1, state root 5jm3itXaXeSNRordzGj614bNEqqMwbEQDJhHhi4y9qXH, txn root E7xJSsJy4F1mXpriSZVnqRPjUwQxXaS3w5vbSoFjVGQs, audit root 9demmNaLp2B9AZuAVeBCQtbAaLJcznwQdAH71bMaxANa, requests ordered 1, discarded 0
node1-1      | 2024-09-11 17:20:39,665|INFO|ordering_service.py|Node1:0 ordered batch request, view no 0, ppSeqNo 7, ledger 1, state root 5jm3itXaXeSNRordzGj614bNEqqMwbEQDJhHhi4y9qXH, txn root E7xJSsJy4F1mXpriSZVnqRPjUwQxXaS3w5vbSoFjVGQs, audit root 9demmNaLp2B9AZuAVeBCQtbAaLJcznwQdAH71bMaxANa, requests ordered 1, discarded 0
node3-1      | 2024-09-11 17:20:39,667|INFO|ordering_service.py|Node3:0 set last ordered as (0, 7)
node4-1      | 2024-09-11 17:20:39,670|INFO|ordering_service.py|Node4:0 set last ordered as (0, 7)
node3-1      | 2024-09-11 17:20:39,671|INFO|ordering_service.py|Node3:0 ordered batch request, view no 0, ppSeqNo 7, ledger 1, state root 5jm3itXaXeSNRordzGj614bNEqqMwbEQDJhHhi4y9qXH, txn root E7xJSsJy4F1mXpriSZVnqRPjUwQxXaS3w5vbSoFjVGQs, audit root 9demmNaLp2B9AZuAVeBCQtbAaLJcznwQdAH71bMaxANa, requests ordered 1, discarded 0
node3-1      | 2024-09-11 17:20:39,671|INFO|ordering_service.py|Node3:1 set last ordered as (0, 4)
node3-1      | 2024-09-11 17:20:39,671|INFO|ordering_service.py|Node3:1 ordered batch request, view no 0, ppSeqNo 4, ledger 1, state root None, txn root None, audit root None, requests ordered 1, discarded 0
node4-1      | 2024-09-11 17:20:39,673|INFO|ordering_service.py|Node4:0 ordered batch request, view no 0, ppSeqNo 7, ledger 1, state root 5jm3itXaXeSNRordzGj614bNEqqMwbEQDJhHhi4y9qXH, txn root E7xJSsJy4F1mXpriSZVnqRPjUwQxXaS3w5vbSoFjVGQs, audit root 9demmNaLp2B9AZuAVeBCQtbAaLJcznwQdAH71bMaxANa, requests ordered 1, discarded 0
webserver-1  | INFO:server.anchor:DOMAIN ledger synced with 9 transaction(s)
node1-1      | 2024-09-11 17:24:24,008|INFO|ordering_service.py|Ledger 0 is not updated for 301 seconds, so its freshness state is going to be updated now
node1-1      | 2024-09-11 17:24:24,013|INFO|ordering_service.py|Ledger 2 is not updated for 301 seconds, so its freshness state is going to be updated now
node3-1      | 2024-09-11 17:24:24,057|INFO|ordering_service.py|Node3:0 set last ordered as (0, 8)
node2-1      | 2024-09-11 17:24:24,058|INFO|ordering_service.py|Node2:0 set last ordered as (0, 8)
node4-1      | 2024-09-11 17:24:24,058|INFO|ordering_service.py|Node4:0 set last ordered as (0, 8)
node1-1      | 2024-09-11 17:24:24,059|INFO|ordering_service.py|Node1:0 set last ordered as (0, 8)
node3-1      | 2024-09-11 17:24:24,060|INFO|ordering_service.py|Node3:0 ordered batch request, view no 0, ppSeqNo 8, ledger 0, state root H1o85bNBQbvp7hSvqFsnKCwW2oWnzMWDHSdD7wVjaAQd, txn root Cv3r9P26vvuKDekhaHSSUW1mBRihUSgTZcAzhmgAMa1A, audit root 9LMsCgh9AiCC7saqH8cmVTRTTcg6xAGJvQSviigckVVq, requests ordered 0, discarded 0
node2-1      | 2024-09-11 17:24:24,061|INFO|ordering_service.py|Node2:0 ordered batch request, view no 0, ppSeqNo 8, ledger 0, state root H1o85bNBQbvp7hSvqFsnKCwW2oWnzMWDHSdD7wVjaAQd, txn root Cv3r9P26vvuKDekhaHSSUW1mBRihUSgTZcAzhmgAMa1A, audit root 9LMsCgh9AiCC7saqH8cmVTRTTcg6xAGJvQSviigckVVq, requests ordered 0, discarded 0
node4-1      | 2024-09-11 17:24:24,061|INFO|ordering_service.py|Node4:0 ordered batch request, view no 0, ppSeqNo 8, ledger 0, state root H1o85bNBQbvp7hSvqFsnKCwW2oWnzMWDHSdD7wVjaAQd, txn root Cv3r9P26vvuKDekhaHSSUW1mBRihUSgTZcAzhmgAMa1A, audit root 9LMsCgh9AiCC7saqH8cmVTRTTcg6xAGJvQSviigckVVq, requests ordered 0, discarded 0
node1-1      | 2024-09-11 17:24:24,062|INFO|ordering_service.py|Node1:0 ordered batch request, view no 0, ppSeqNo 8, ledger 0, state root H1o85bNBQbvp7hSvqFsnKCwW2oWnzMWDHSdD7wVjaAQd, txn root Cv3r9P26vvuKDekhaHSSUW1mBRihUSgTZcAzhmgAMa1A, audit root 9LMsCgh9AiCC7saqH8cmVTRTTcg6xAGJvQSviigckVVq, requests ordered 0, discarded 0
node2-1      | 2024-09-11 17:24:24,063|INFO|ordering_service.py|Node2:0 set last ordered as (0, 9)
node4-1      | 2024-09-11 17:24:24,064|INFO|ordering_service.py|Node4:0 set last ordered as (0, 9)
node3-1      | 2024-09-11 17:24:24,065|INFO|ordering_service.py|Node3:0 set last ordered as (0, 9)
node2-1      | 2024-09-11 17:24:24,066|INFO|ordering_service.py|Node2:0 ordered batch request, view no 0, ppSeqNo 9, ledger 2, state root DfNLmH4DAHTKv63YPFJzuRdeEtVwF5RtVnvKYHd8iLEA, txn root GKot5hBsd81kMupNCXHaqbhv3huEbxAFMLnpcX2hniwn, audit root CW4xYF2NE7mFyrLGJ9ktnnFz7eY1hEoNoduL3jKdekZR, requests ordered 0, discarded 0
node4-1      | 2024-09-11 17:24:24,067|INFO|ordering_service.py|Node4:0 ordered batch request, view no 0, ppSeqNo 9, ledger 2, state root DfNLmH4DAHTKv63YPFJzuRdeEtVwF5RtVnvKYHd8iLEA, txn root GKot5hBsd81kMupNCXHaqbhv3huEbxAFMLnpcX2hniwn, audit root CW4xYF2NE7mFyrLGJ9ktnnFz7eY1hEoNoduL3jKdekZR, requests ordered 0, discarded 0
node1-1      | 2024-09-11 17:24:24,067|INFO|ordering_service.py|Node1:0 set last ordered as (0, 9)
node3-1      | 2024-09-11 17:24:24,069|INFO|ordering_service.py|Node3:0 ordered batch request, view no 0, ppSeqNo 9, ledger 2, state root DfNLmH4DAHTKv63YPFJzuRdeEtVwF5RtVnvKYHd8iLEA, txn root GKot5hBsd81kMupNCXHaqbhv3huEbxAFMLnpcX2hniwn, audit root CW4xYF2NE7mFyrLGJ9ktnnFz7eY1hEoNoduL3jKdekZR, requests ordered 0, discarded 0
node1-1      | 2024-09-11 17:24:24,070|INFO|ordering_service.py|Node1:0 ordered batch request, view no 0, ppSeqNo 9, ledger 2, state root DfNLmH4DAHTKv63YPFJzuRdeEtVwF5RtVnvKYHd8iLEA, txn root GKot5hBsd81kMupNCXHaqbhv3huEbxAFMLnpcX2hniwn, audit root CW4xYF2NE7mFyrLGJ9ktnnFz7eY1hEoNoduL3jKdekZR, requests ordered 0, discarded 0
node1-1      | 2024-09-11 17:25:40,015|INFO|ordering_service.py|Ledger 1 is not updated for 301 seconds, so its freshness state is going to be updated now
node2-1      | 2024-09-11 17:25:40,063|INFO|ordering_service.py|Node2:0 set last ordered as (0, 10)
node3-1      | 2024-09-11 17:25:40,063|INFO|ordering_service.py|Node3:0 set last ordered as (0, 10)
node4-1      | 2024-09-11 17:25:40,063|INFO|ordering_service.py|Node4:0 set last ordered as (0, 10)
node1-1      | 2024-09-11 17:25:40,065|INFO|ordering_service.py|Node1:0 set last ordered as (0, 10)
node2-1      | 2024-09-11 17:25:40,067|INFO|ordering_service.py|Node2:0 ordered batch request, view no 0, ppSeqNo 10, ledger 1, state root 5jm3itXaXeSNRordzGj614bNEqqMwbEQDJhHhi4y9qXH, txn root E7xJSsJy4F1mXpriSZVnqRPjUwQxXaS3w5vbSoFjVGQs, audit root 42FmsjCA4YYADR5Ru9w95MvHiGAG5W9yehxDXJeR2HwX, requests ordered 0, discarded 0
node3-1      | 2024-09-11 17:25:40,067|INFO|ordering_service.py|Node3:0 ordered batch request, view no 0, ppSeqNo 10, ledger 1, state root 5jm3itXaXeSNRordzGj614bNEqqMwbEQDJhHhi4y9qXH, txn root E7xJSsJy4F1mXpriSZVnqRPjUwQxXaS3w5vbSoFjVGQs, audit root 42FmsjCA4YYADR5Ru9w95MvHiGAG5W9yehxDXJeR2HwX, requests ordered 0, discarded 0
node4-1      | 2024-09-11 17:25:40,067|INFO|ordering_service.py|Node4:0 ordered batch request, view no 0, ppSeqNo 10, ledger 1, state root 5jm3itXaXeSNRordzGj614bNEqqMwbEQDJhHhi4y9qXH, txn root E7xJSsJy4F1mXpriSZVnqRPjUwQxXaS3w5vbSoFjVGQs, audit root 42FmsjCA4YYADR5Ru9w95MvHiGAG5W9yehxDXJeR2HwX, requests ordered 0, discarded 0
node1-1      | 2024-09-11 17:25:40,068|INFO|ordering_service.py|Node1:0 ordered batch request, view no 0, ppSeqNo 10, ledger 1, state root 5jm3itXaXeSNRordzGj614bNEqqMwbEQDJhHhi4y9qXH, txn root E7xJSsJy4F1mXpriSZVnqRPjUwQxXaS3w5vbSoFjVGQs, audit root 42FmsjCA4YYADR5Ru9w95MvHiGAG5W9yehxDXJeR2HwX, requests ordered 0, discarded 0
node1-1      | 2024-09-11 17:29:25,003|INFO|ordering_service.py|Ledger 0 is not updated for 301 seconds, so its freshness state is going to be updated now
node1-1      | 2024-09-11 17:29:25,019|INFO|ordering_service.py|Ledger 2 is not updated for 301 seconds, so its freshness state is going to be updated now
node4-1      | 2024-09-11 17:29:25,065|INFO|ordering_service.py|Node4:0 set last ordered as (0, 11)
node2-1      | 2024-09-11 17:29:25,065|INFO|ordering_service.py|Node2:0 set last ordered as (0, 11)
node1-1      | 2024-09-11 17:29:25,065|INFO|ordering_service.py|Node1:0 set last ordered as (0, 11)
node3-1      | 2024-09-11 17:29:25,067|INFO|ordering_service.py|Node3:0 set last ordered as (0, 11)
node4-1      | 2024-09-11 17:29:25,068|INFO|ordering_service.py|Node4:0 ordered batch request, view no 0, ppSeqNo 11, ledger 0, state root H1o85bNBQbvp7hSvqFsnKCwW2oWnzMWDHSdD7wVjaAQd, txn root Cv3r9P26vvuKDekhaHSSUW1mBRihUSgTZcAzhmgAMa1A, audit root GUcKocdhbsAP17YtpciLm5qpRiBwKSyqdmqtu2YPgKYj, requests ordered 0, discarded 0
node2-1      | 2024-09-11 17:29:25,069|INFO|ordering_service.py|Node2:0 ordered batch request, view no 0, ppSeqNo 11, ledger 0, state root H1o85bNBQbvp7hSvqFsnKCwW2oWnzMWDHSdD7wVjaAQd, txn root Cv3r9P26vvuKDekhaHSSUW1mBRihUSgTZcAzhmgAMa1A, audit root GUcKocdhbsAP17YtpciLm5qpRiBwKSyqdmqtu2YPgKYj, requests ordered 0, discarded 0
node1-1      | 2024-09-11 17:29:25,069|INFO|ordering_service.py|Node1:0 ordered batch request, view no 0, ppSeqNo 11, ledger 0, state root H1o85bNBQbvp7hSvqFsnKCwW2oWnzMWDHSdD7wVjaAQd, txn root Cv3r9P26vvuKDekhaHSSUW1mBRihUSgTZcAzhmgAMa1A, audit root GUcKocdhbsAP17YtpciLm5qpRiBwKSyqdmqtu2YPgKYj, requests ordered 0, discarded 0
node3-1      | 2024-09-11 17:29:25,070|INFO|ordering_service.py|Node3:0 ordered batch request, view no 0, ppSeqNo 11, ledger 0, state root H1o85bNBQbvp7hSvqFsnKCwW2oWnzMWDHSdD7wVjaAQd, txn root Cv3r9P26vvuKDekhaHSSUW1mBRihUSgTZcAzhmgAMa1A, audit root GUcKocdhbsAP17YtpciLm5qpRiBwKSyqdmqtu2YPgKYj, requests ordered 0, discarded 0
node4-1      | 2024-09-11 17:29:25,071|INFO|ordering_service.py|Node4:0 set last ordered as (0, 12)
node2-1      | 2024-09-11 17:29:25,071|INFO|ordering_service.py|Node2:0 set last ordered as (0, 12)
node4-1      | 2024-09-11 17:29:25,074|INFO|ordering_service.py|Node4:0 ordered batch request, view no 0, ppSeqNo 12, ledger 2, state root DfNLmH4DAHTKv63YPFJzuRdeEtVwF5RtVnvKYHd8iLEA, txn root GKot5hBsd81kMupNCXHaqbhv3huEbxAFMLnpcX2hniwn, audit root 7hvS6t1isWu1TfYVzuhGiXuKDEGz8j5UU1pZTWxydRWT, requests ordered 0, discarded 0
node2-1      | 2024-09-11 17:29:25,074|INFO|ordering_service.py|Node2:0 ordered batch request, view no 0, ppSeqNo 12, ledger 2, state root DfNLmH4DAHTKv63YPFJzuRdeEtVwF5RtVnvKYHd8iLEA, txn root GKot5hBsd81kMupNCXHaqbhv3huEbxAFMLnpcX2hniwn, audit root 7hvS6t1isWu1TfYVzuhGiXuKDEGz8j5UU1pZTWxydRWT, requests ordered 0, discarded 0
node1-1      | 2024-09-11 17:29:25,074|INFO|ordering_service.py|Node1:0 set last ordered as (0, 12)
node3-1      | 2024-09-11 17:29:25,075|INFO|ordering_service.py|Node3:0 set last ordered as (0, 12)
node1-1      | 2024-09-11 17:29:25,077|INFO|ordering_service.py|Node1:0 ordered batch request, view no 0, ppSeqNo 12, ledger 2, state root DfNLmH4DAHTKv63YPFJzuRdeEtVwF5RtVnvKYHd8iLEA, txn root GKot5hBsd81kMupNCXHaqbhv3huEbxAFMLnpcX2hniwn, audit root 7hvS6t1isWu1TfYVzuhGiXuKDEGz8j5UU1pZTWxydRWT, requests ordered 0, discarded 0
node3-1      | 2024-09-11 17:29:25,078|INFO|ordering_service.py|Node3:0 ordered batch request, view no 0, ppSeqNo 12, ledger 2, state root DfNLmH4DAHTKv63YPFJzuRdeEtVwF5RtVnvKYHd8iLEA, txn root GKot5hBsd81kMupNCXHaqbhv3huEbxAFMLnpcX2hniwn, audit root 7hvS6t1isWu1TfYVzuhGiXuKDEGz8j5UU1pZTWxydRWT, requests ordered 0, discarded 0
```
