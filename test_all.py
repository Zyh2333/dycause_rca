"""Test and compare all algorithms
"""
import sys
import time

# import numpy as np

from main_cloud_ranger import test_cloud_ranger
from main_dycause import test_dycause
from main_tbac import test_tbac
from main_monitor_rank import test_monitor_rank

# from main_facgraph import test_facgraph
from main_netmedic import test_netmedic

if __name__ == '__main__':
    # pymicro test suite
    print("\n{:!^80}\n".format(" Pymicro Test Suite "))
    # 0722
    entry_point_list = [6,6,6,6,6,6,6,6,6,6,6]
    # 0723
    # entry_point_list = [6,6,6,6,6,6,6,6,6,6,6,6,6,6]
    entry_point = 6
    # 0722
    true_root_cause = [2,2,3,4,5,9,9,7,6,5,2]
    # 0723
    # true_root_cause = [2,2,3,4,4,5,5,6,7,7,8,9,9,10]
    verbose = 1

    # test_tbac("pymicro", pc_aggregate=37, frontend=16, true_root_cause=[1], 
    #     verbose=verbose)

    acc_tbac_total = 0
    acc_monitor_rank_total = 0
    acc_cloud_total = 0
    acc_netmedic_total = 0
    acc_dycause_total = 0
    for i in range(len(true_root_cause)):
        print('根因根因！！！:' + str(true_root_cause[i]))
        _, acc_tbac = test_tbac(i, "microIRC", pc_aggregate=37, frontend=entry_point_list[i], true_root_cause=[true_root_cause[i]], 
            verbose=verbose)

        # test_monitor_rank(
        #     "pymicro",
        #     pc_aggregate=5,
        #     testrun_round=1,
        #     frontend=16,
        #     true_root_cause=true_root_cause,
        #     rho=0.2,
        #     save_data_fig=False,
        #     verbose=verbose,
        # )

        _, acc_monitor = test_monitor_rank(
            i,
            "microIRC",
            pc_aggregate=5,
            testrun_round=1,
            frontend=entry_point_list[i],
            true_root_cause=[true_root_cause[i]],
            rho=0.2,
            save_data_fig=False,
            verbose=verbose,
        )

        # test_cloud_ranger(
        #     data_source="pymicro",
        #     pc_aggregate=5,
        #     pc_alpha=0.1,
        #     testrun_round=1,
        #     frontend=16,
        #     true_root_cause=true_root_cause,
        #     beta=0.2,
        #     rho=0.2,
        #     save_data_fig=False,
        #     verbose=verbose,
        # )

        _, acc_cloud = test_cloud_ranger(
            i,
            data_source="microIRC",
            pc_aggregate=5,
            pc_alpha=0.1,
            testrun_round=1,
            frontend=entry_point_list[i],
            true_root_cause=[true_root_cause[i]],
            beta=0.2,
            rho=0.2,
            save_data_fig=False,
            verbose=verbose,
        )

        # test_netmedic(
        #     data_source="pymicro",
        #     history_range=(600, 800),
        #     current_range=(800, 1200),
        #     bin_size=100,
        #     affected_node=16,
        #     true_root_cause=true_root_cause,
        #     verbose=verbose,
        # )

        _, acc_netmedic = test_netmedic(
            i,
            data_source="microIRC",
            history_range=(0, 120),
            current_range=(120, 240),
            bin_size=60,
            affected_node=10,
            true_root_cause=[true_root_cause[i]],
            verbose=verbose,
        )

        # # # Acc=93.75 in the following parameters

        # test_dycause(
        #     # Data params
        #     data_source="pymicro", 
        #     aggre_delta=1,
        #     start_time=1200,
        #     before_length=100,
        #     after_length=0,
        #     # Granger interval based graph construction params
        #     step=30,
        #     significant_thres=0.1,
        #     lag=9,
        #     auto_threshold_ratio=0.8,
        #     # Root cause analysis params
        #     testrun_round=1,
        #     frontend=entry_point_list[0],
        #     true_root_cause=true_root_cause,
        #     # Debug params
        #     plot_figures=False,
        #     verbose=2,
        # )

        _, acc_dycause = test_dycause(
            i,
            # Data params
            data_source="microIRC", 
            aggre_delta=1,
            start_time=120,
            before_length=60,
            after_length=120,
            # Granger interval based graph construction params
            step=30,
            significant_thres=0.1,
            lag=9,
            auto_threshold_ratio=0.5,
            # Root cause analysis params
            testrun_round=1,
            frontend=entry_point_list[i],
            true_root_cause=[true_root_cause[i]],
            # Debug params
            plot_figures=False,
            verbose=2,
        )
        acc_cloud_total += acc_cloud
        acc_dycause_total += acc_dycause
        acc_tbac_total += acc_tbac
        acc_monitor_rank_total += acc_monitor
        acc_netmedic_total += acc_netmedic
    
    print('acc_tbac_total:' + str(acc_tbac_total / len(true_root_cause)))
    print('acc_cloud_total:' + str(acc_cloud_total / len(true_root_cause)))
    print('acc_dycause_total:' + str(acc_dycause_total / len(true_root_cause)))
    print('acc_monitor_rank_total:' + str(acc_monitor_rank_total / len(true_root_cause)))
    print('acc_netmedic_total:' + str(acc_netmedic_total / len(true_root_cause)))

    # real_micro_service test suite
    # print("\n{:!^80}\n".format(" Real Micro Service Test Suite "))

    # entry_point_list = [14]
    # true_root_cause = [6, 28, 30, 31]
    # verbose=3
    # # true_root_cause_1 = [28]

    # # tic = time.time()
    # test_tbac(
    #     "real_micro_service", 
    #     pc_aggregate=12, 
    #     pc_alpha=0.05,
    #     frontend=entry_point_list[0], 
    #     true_root_cause=true_root_cause,
    #     verbose=verbose,
    #     runtime_debug=True,
    # )
    # # # toc = time.time() - tic
    # # # print('Used time: {:.4f} seconds'.format(toc))

    # # # tic = time.time()
    # test_netmedic(
    #     data_source="real_micro_service",
    #     history_range=(0, 200),
    #     current_range=(4600, 4800),
    #     bin_size=10,
    #     affected_node=entry_point_list[0],
    #     true_root_cause=true_root_cause,
    #     verbose=verbose,
    #     runtime_debug=True,
    # )
    # # toc = time.time() - tic
    # # print('Used time: {:.4f} seconds'.format(toc))

    # # tic = time.time()
    # test_monitor_rank(
    #     "real_micro_service",
    #     pc_aggregate=20, # 8
    #     pc_alpha=0.1, 
    #     testrun_round=5,
    #     rho=0.1,  # rho=0.4
    #     frontend=entry_point_list[0],
    #     true_root_cause=true_root_cause,
    #     save_data_fig=False,
    #     verbose=verbose,
    #     runtime_debug=True
    # )
    # # toc = time.time() - tic
    # # print('Used time: {:.4f} seconds'.format(toc))

    # # tic = time.time()
    # test_cloud_ranger(
    #     data_source="real_micro_service",
    #     pc_aggregate=20,
    #     pc_alpha=0.1,
    #     testrun_round=5,
    #     beta=0.1,
    #     rho=0.1,
    #     frontend=entry_point_list[0],
    #     true_root_cause=true_root_cause,
    #     verbose=verbose,
    #     runtime_debug=True
    # )
    # # toc = time.time() - tic
    # # print('Used time: {:.4f} seconds'.format(toc))

    # # granger causal interval extend test
    # # tic = time.time()
    # test_dycause(
    #     # Data params
    #     data_source="real_micro_service",
    #     aggre_delta=1,
    #     start_time=None,
    #     before_length=0,
    #     after_length=280,
    #     # Granger interval based graph construction params
    #     step=70,
    #     significant_thres=0.1,
    #     lag=5, # must satisfy: step > 3 * lag + 1
    #     auto_threshold_ratio = 0.5,
    #     # Root cause analysis params
    #     testrun_round=1,
    #     frontend=entry_point_list[0],
    #     true_root_cause=true_root_cause,
    #     max_path_length=None,
    #     mean_method="harmonic",
    #     topk_path=150,
    #     num_sel_node=3,
    #     # Debug params
    #     plot_figures=False,
    #     verbose=verbose,
    #     runtime_debug=False,
    # )
    # # toc = time.time() - tic
    # # print('Used time: {:.4f} seconds'.format(toc))
