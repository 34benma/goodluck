#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright [2016-2026] wangcheng(wantedonline@outlook.com)

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


 ,-.           . ,            ,
/              | |            |
| -. ,-. ,-. ,-| |    . . ,-. | ,
\  | | | | | | | |    | | |   |<
 `-' `-' `-' `-' `--' `-` `-' ' `

http://www.kammerl.de/ascii/AsciiSignature.php
(Font: 'shimrod')

Author: LouisWang(wantedonline@outlook.com)
Version:0.0.1
Date: 2017.06.15
Version:0.0.2
Date: 2017.06.16
Version:0.0.3
Date: 2017.06.16
"""

import sys
_p_version_is_3 = sys.version.startswith("3")
if _p_version_is_3:
    import configparser as ConfigParser
else:
    import ConfigParser
import os

_version = "0_0_3"
_version_str = "V0.0.3"
_soft_name = '''
 ,-.           . ,            ,
/              | |            |
| -. ,-. ,-. ,-| |    . . ,-. | ,
\  | | | | | | | |    | | |   |<
 `-' `-' `-' `-' `--' `-` `-' ' `
 
'''

_copyright = '''
  Copyright [2016-2026] wangcheng(wantedonline@outlook.com)

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

'''

ext_data = """
# -*- coding: utf-8 -*-

from mercurial import cmdutil
from mercurial import commands
from mercurial.i18n import _
from mercurial import encoding

import locale
import os

cmdtable = {}
command = cmdutil.command(cmdtable)

# common command options

globalopts = [
    ('R', 'repository', '',
     _('repository root directory or name of overlay bundle file'),
     _('REPO')),
    ('', 'cwd', '',
     _('change working directory'), _('DIR')),
    ('y', 'noninteractive', None,
     _('do not prompt, automatically pick the first choice for all prompts')),
    ('q', 'quiet', None, _('suppress output')),
    ('v', 'verbose', None, _('enable additional output')),
    ('', 'config', [],
     _('set/override config option (use \\'section.name=value\\')'),
     _('CONFIG')),
    ('', 'debug', None, _('enable debugging output')),
    ('', 'debugger', None, _('start debugger')),
    ('', 'encoding', encoding.encoding, _('set the charset encoding'),
     _('ENCODE')),
    ('', 'encodingmode', encoding.encodingmode,
     _('set the charset encoding mode'), _('MODE')),
    ('', 'traceback', None, _('always print a traceback on exception')),
    ('', 'time', None, _('time how long the command takes')),
    ('', 'profile', None, _('print command execution profile')),
    ('', 'version', None, _('output version information and exit')),
    ('h', 'help', None, _('display help and exit')),
    ('', 'hidden', False, _('consider hidden changesets')),
]

dryrunopts = [('n', 'dry-run', None,
               _('do not perform actions, just print output'))]

remoteopts = [
    ('e', 'ssh', '',
     _('specify ssh command to use'), _('CMD')),
    ('', 'remotecmd', '',
     _('specify hg command to run on the remote side'), _('CMD')),
    ('', 'insecure', None,
     _('do not verify server certificate (ignoring web.cacerts config)')),
]

walkopts = [
    ('I', 'include', [],
     _('include names matching the given patterns'), _('PATTERN')),
    ('X', 'exclude', [],
     _('exclude names matching the given patterns'), _('PATTERN')),
]

commitopts = [
    ('m', 'message', '',
     _('use text as commit message'), _('TEXT')),
    ('l', 'logfile', '',
     _('read commit message from file'), _('FILE')),
]

commitopts2 = [
    ('d', 'date', '',
     _('record the specified date as commit date'), _('DATE')),
    ('u', 'user', '',
     _('record the specified user as committer'), _('USER')),
]

# hidden for now
formatteropts = [
    ('T', 'template', '',
     _('display with template (EXPERIMENTAL)'), _('TEMPLATE')),
]

templateopts = [
    ('', 'style', '',
     _('display using template map file (DEPRECATED)'), _('STYLE')),
    ('T', 'template', '',
     _('display with template'), _('TEMPLATE')),
]

logopts = [
    ('p', 'patch', None, _('show patch')),
    ('g', 'git', None, _('use git extended diff format')),
    ('l', 'limit', '',
     _('limit number of changes displayed'), _('NUM')),
    ('M', 'no-merges', None, _('do not show merges')),
    ('', 'stat', None, _('output diffstat-style summary of changes')),
    ('G', 'graph', None, _("show the revision DAG")),
] + templateopts

diffopts = [
    ('a', 'text', None, _('treat all files as text')),
    ('g', 'git', None, _('use git extended diff format')),
    ('', 'nodates', None, _('omit dates from diff headers'))
]

diffwsopts = [
    ('w', 'ignore-all-space', None,
     _('ignore white space when comparing lines')),
    ('b', 'ignore-space-change', None,
     _('ignore changes in the amount of white space')),
    ('B', 'ignore-blank-lines', None,
     _('ignore changes whose lines are all blank')),
    ]

diffopts2 = [
    ('', 'noprefix', None, _('omit a/ and b/ prefixes from filenames')),
    ('p', 'show-function', None, _('show which function each change is in')),
    ('', 'reverse', None, _('produce a diff that undoes the changes')),
    ] + diffwsopts + [
    ('U', 'unified', '',
     _('number of lines of context to show'), _('NUM')),
    ('', 'stat', None, _('output diffstat-style summary of changes')),
    ('', 'root', '', _('produce diffs relative to subdirectory'), _('DIR')),
]

mergetoolopts = [
    ('t', 'tool', '', _('specify merge tool')),
]

similarityopts = [
    ('s', 'similarity', '',
     _('guess renamed files by similarity (0<=s<=100)'), _('SIMILARITY'))
]

subrepoopts = [
    ('S', 'subrepos', None,
     _('recurse into subrepositories'))
]

_is_zh = locale.getdefaultlocale()[0] == 'zh_CN'

_lang_zh = {
    "tip_update_branch" : "切换分支，当前分支和要切换的分支",
    "prompt_update_branch" : "切换分支后先拉取最新代码?(y/n)默认y" + os.linesep,
    "prompt_update" : "更新本地代码前是否拉取最新代码(y/n),默认y" + os.linesep,
    "tip_pull_new" : "拉取最新代码..." + os.linesep,
    "tip_merge_before" : "正在进行代码合并操作，请检查当前分支和待合并的分支是否正确...",
    "prompt_sure_merge" : "是否确认完毕，如果无误，请输入确认y(y/n)" + os.linesep,
    "tip_begin_merge" : "准备合并分支代码..." + os.linesep,
    "tip_finished_merge" : "代码合并完毕" + os.linesep,
    "tip_cancel_merge" : "放弃本次合并..." + os.linesep,
    "prompt_sure_commit" : "确认提交本次修改吗？(y/n),修改提交的分支为 ",
    "prompt_sure_compare" : "是否已经比对过本次代码的新老版本(y/n)" + os.linesep,
    "prompt_sure_finished_compare" : "代码比对完毕?(y/n)" + os.linesep,
    "tip_compare_code" : "请仔细比对待提交代码(- 代表变更前 + 代表变更后)" + os.linesep,
    "tip_before_commit" : "准备提交本次修改..." + os.linesep,
    "tip_finished_commit":  "本次修改已经提交到本地" + os.linesep,
    "tip_cancel_commit" : "放弃本次本地修改..." + os.linesep,
    "prompt_sure_push" : "确认要提交代码到代码库吗?(y/n),推送的分支为 ",
    "tip_before_push" : "准备推送代码到代码库..." + os.linesep,
    "tip_after_push" : "代码推送完毕" + os.linesep,
    "tip_cancel_push" : "放弃本次提交" + os.linesep,
    "prompt_sure_branch" : "父分支是否正确?(y/n)" + os.linesep,
    "tip_finished_branch" : "新分支创建完毕" + os.linesep,
    "tip_cancel_branch" : "放弃创建新分支" + os.linesep,
    "tip_new_branch" : "正在进行分支创建操作，分支信息 ",
}

_lang_en = {
    "tip_update_branch" : "switch branch, current branch and switch to branch is ",
    "prompt_update_branch" : "after switch to new branch, pull code first?(y/n),default is y" + os.linesep,
    "prompt_update" : "pull newest code before update locale code?(y/n),default is y" + os.linesep,
    "tip_pull_new" : "pull newest code ing..." + os.linesep,
    "tip_merge_before" : "you are doing merge code, please check and be sure the branch of now and need merge branch is right...",
    "prompt_sure_merge" : "are you sure? if your have sured, please input y (y/n)" + os.linesep,
    "tip_begin_merge" : "begin to merge branch code..." + os.linesep,
    "tip_finished_merge" : "code merge finished" + os.linesep,
    "tip_cancel_merge" : "merge canceled" + os.linesep,
    "prompt_sure_commit" : "are you sure all the modified?(y/n), you will commit to branch ",
    "prompt_sure_compare" : "have you compared the code with new and old version?(y/n)" + os.linesep,
    "prompt_sure_finished_compare":"compared all code?(y/n)" + os.linesep,
    "tip_compare_code" : "please compare your code carefully(- means before modified, + means after modified)" + os.linesep,
    "tip_before_commit" : "begin to commit all the modify..." + os.linesep,
    "tip_finished_commit" : "finished commit your code to local repo" + os.linesep,
    "tip_cancel_commit" : "cancel this commit to local repo" + os.linesep,
    "prompt_sure_push" : "are you sure push your code to remote repo?(y/n) push to branch ",
    "tip_before_push" : "begin to push your code to remote repo..." + os.linesep,
    "tip_after_push" : "code push finished" + os.linesep,
    "tip_cancel_push" : "this push canceled" + os.linesep,
    "prompt_sure_branch" : "parent branch is right?(y/n)" + os.linesep,
    "tip_finished_branch" : "new branch created" + os.linesep,
    "tip_cancel_branch" : "cancel create new branch" + os.linesep,
    "tip_new_branch" : "you are creating new branch, branch info ",

}



@command('^update|up|checkout|co',
    [('C', 'clean', None, _('discard uncommitted changes (no backup)')),
    ('c', 'check', None,
     _('update across branches if no uncommitted changes')),
    ('d', 'date', '', _('tipmost revision matching date'), _('DATE')),
    ('r', 'rev', '', _('revision'), _('REV'))
     ] + mergetoolopts,
    _('[-c] [-C] [-d DATE] [[-r] REV]'))
def update(ui, repo, node=None, rev=None, clean=False, date=None, check=False,
           tool=None,**opts):
    current_branch = repo.dirstate.branch()
    if node and node != current_branch:
        #在切换分支
        ui.warn(_get_tip("tip_update_branch") + "current branch:" + current_branch + ",switch to branch: " + node + os.linesep)
    else:
        # 仅仅是更新当前分支
        resp = _getResp(ui.prompt(_get_tip("prompt_update"),default="y"))
        if resp:
            ui.write(_get_tip("tip_pull_new"))
            commands.pull(ui,repo)
    commands.update(ui, repo, node, rev, clean, date, check,
           tool, **opts)
    if node and node != current_branch:
        if _getResp(ui.prompt(_get_tip("prompt_update_branch"))):
            commands.pull(ui, repo)

@command('^merge',
    [('f', 'force', None,
      _('force a merge including outstanding changes (DEPRECATED)')),
    ('r', 'rev', '', _('revision to merge'), _('REV')),
    ('P', 'preview', None,
     _('review revisions to merge (no merge is performed)'))
     ] + mergetoolopts,
    _('[-P] [-f] [[-r] REV]'))
def merge(ui, repo, node=None, **opts):
    current_branch = repo.dirstate.branch()
    ui.warn(_get_tip("tip_merge_before") + "current branch:" + current_branch + ",merged branch: " + node + os.linesep)
    resp = _getResp(ui.prompt(_get_tip("prompt_sure_merge"),default="n"))
    if resp:
        ui.write(_get_tip("tip_begin_merge"))
        commands.merge(ui, repo, node, **opts)
        ui.write(_get_tip("tip_finished_merge"))
    else:
        ui.write(_get_tip("tip_cancel_merge"))

@command('^commit|ci',
    [('A', 'addremove', None,
     _('mark new/missing files as added/removed before committing')),
    ('', 'close-branch', None,
     _('mark a branch as closed, hiding it from the branch list')),
    ('', 'amend', None, _('amend the parent of the working directory')),
    ('s', 'secret', None, _('use the secret phase for committing')),
    ('e', 'edit', None, _('invoke editor on commit messages')),
    ('i', 'interactive', None, _('use interactive mode')),
    ] + walkopts + commitopts + commitopts2 + subrepoopts,
    _('[OPTION]... [FILE]...'),
    inferrepo=True)
def commit(ui, repo, *pats, **opts):
    current_branch = repo.dirstate.branch()
    resp = _getResp(ui.prompt(_get_tip("prompt_sure_commit") + current_branch + os.linesep, default="n"))
    if resp:
        resp2 = _getResp(ui.prompt(_get_tip("prompt_sure_compare"),default="n"))
        if not resp2:
            commands.diff(ui, repo, *pats,git="--git")

        while not _getResp(ui.prompt(_get_tip("prompt_sure_finished_compare"),default="n")):
            ui.write(_get_tip("tip_compare_code"))
            commands.diff(ui, repo, *pats, git="--git")

        ui.write(_get_tip("tip_before_commit"))
        commands.commit(ui, repo, *pats, **opts)
        ui.write(_get_tip("tip_finished_commit"))
    else:
        ui.write(_get_tip("tip_cancel_commit"))

@command('^push',
    [('f', 'force', None, _('force push')),
    ('r', 'rev', [],
     _('a changeset intended to be included in the destination'),
     _('REV')),
    ('B', 'bookmark', [], _("bookmark to push"), _('BOOKMARK')),
    ('b', 'branch', [],
     _('a specific branch you would like to push'), _('BRANCH')),
    ('', 'new-branch', False, _('allow pushing a new branch')),
    ] + remoteopts,
    _('[-f] [-r REV]... [-e CMD] [--remotecmd CMD] [DEST]'))
def push(ui, repo, dest=None, **opts):
    current_branch = repo.dirstate.branch()
    resp = _getResp(ui.prompt(_get_tip("prompt_sure_push") + current_branch + os.linesep,default="n"))
    if resp:
        ui.warn(_get_tip("tip_before_push"))
        commands.push(ui, repo, dest, **opts)
        ui.write(_get_tip("tip_after_push"))
    else:
        ui.write(_get_tip("tip_cancel_push"))

@command('branch',
    [('f', 'force', None,
     _('set branch name even if it shadows an existing branch')),
    ('C', 'clean', None, _('reset branch name to parent branch name'))],
    _('[-fC] [NAME]'))
def branch(ui, repo, label=None, **opts):
    if label:
        current_branch = repo.dirstate.branch()
        ui.warn(_get_tip("tip_new_branch") + "current branch: " + current_branch + ",new branch: " + label + os.linesep)
        resp = _getResp(ui.prompt(_get_tip("prompt_sure_branch"),default="n"))
        if resp:
            commands.branch(ui, repo, label, **opts)
            ui.write(_get_tip("tip_finished_branch"))
        else:
            ui.write(_get_tip("tip_cancel_branch"))
    commands.branch(ui, repo, label, **opts)


def _getResp(resp):
    return resp in ("y","Y","YES","Yes","yes","1")

def _get_tip(key):
    if _is_zh:
        return _lang_zh.get(key)
    return _lang_en.get(key)
"""

def get_ext_file(ext_path):
    with open(ext_path, 'wb') as f:
        if _p_version_is_3:
            f.write(bytes(ext_data,'utf8'))
        else:
            f.write(ext_data)


def open_color_ext(config):
    """
    开启并设置颜色高亮插件
    """
    config.set('extensions','color','')
    secs = config.sections()
    if 'color' not in secs:
        config.add_section('color')
    config.set('color', 'diff.diffline','bold')
    config.set('color', 'diff.extended','cyan bold')
    config.set('color', 'diff.file_a','red bold')
    config.set('color', 'diff.file_b','green bold')
    config.set('color', 'diff.hunk','magenta')
    config.set('color', 'diff.deleted','red')
    config.set('color', 'diff.inserted','green')
    config.set('color', 'diff.changed','white')
    config.set('color', 'diff.trailingwhitespace','bold red_background')
    config.set('color', 'status.modified','blue bold underline')
    config.set('color', 'status.added','green bold')
    config.set('color', 'status.removed','red bold')
    config.set('color', 'status.deleted','cyan bold underline')
    config.set('color', 'status.unknown','magenta bold underline')
    config.set('color', 'status.ignored','black bold')


def set_hgrc(ext_path):
    """
    配置hgrc，启用插件
    """
    config = ConfigParser.RawConfigParser()
    hgrc_path = os.path.expanduser('~/.hgrc')
    # 是否有这个文件
    if os.path.isfile(hgrc_path):
        config.read(hgrc_path)
        secs = config.sections()
        if 'extensions' not in secs:
            config.add_section('extensions')
    else:
        config.add_section('extensions')

    config.set('extensions', 'goodluck', ext_path)
    # 开启颜色高亮插件
    open_color_ext(config)
    if _p_version_is_3:
        with open(hgrc_path, 'w', encoding='utf8') as configfile:
            config.write(configfile)
    else:
        with open(hgrc_path, 'wb') as configfile:
            config.write(configfile)


def main():
    file_name = '.good_luck_' + _version + '.py'
    if len(sys.argv) == 2:
        ext_path = sys.argv[1]
        if os.path.isdir(ext_path):
            ext_path = os.path.join(ext_path, file_name)
        else:
            print("%s,不是一个有效路径" % ext_path)
            return
    else:
        ext_path = os.path.expanduser('~/%s' % file_name)
    get_ext_file(ext_path)
    set_hgrc(ext_path)

    print(_soft_name + _version_str)
    print(_copyright)




if __name__ == '__main__':
    main()
