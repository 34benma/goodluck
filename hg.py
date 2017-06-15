# coding: utf-8
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
"""

from mercurial import cmdutil
from mercurial import commands
from mercurial.i18n import _
from mercurial import encoding


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
     _('set/override config option (use \'section.name=value\')'),
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
    resp = _getResp(ui.prompt("更新本地代码前是否拉取最新代码(y/n),默认y\\n",default="y"))
    if resp:
        ui.write("拉取最新代码...\\n")
        commands.pull(ui,repo, **opts)
    commands.update(ui, repo, node, rev, clean, date, check,
           tool, **opts)

@command('^merge',
    [('f', 'force', None,
      _('force a merge including outstanding changes (DEPRECATED)')),
    ('r', 'rev', '', _('revision to merge'), _('REV')),
    ('P', 'preview', None,
     _('review revisions to merge (no merge is performed)'))
     ] + mergetoolopts,
    _('[-P] [-f] [[-r] REV]'))
def merge(ui, repo, node=None, **opts):
    ui.write("正在进行代码合并操作，请检查当前分支和待合并的分支是否正确...\\n")
    resp = _getResp(ui.prompt("是否确认完毕，如果无误，请输入确认y(y/n)\\n"))
    if resp:
        ui.write("准备合并分支代码...\\n")
        commands.merge(ui, repo, node, **opts)
        ui.write("代码合并完毕\\n")
    else:
        ui.write("放弃本次合并...\\n")

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
    resp = _getResp(ui.prompt("确认提交本次修改吗？(y/n)\\n", default="n"))
    if resp:
        resp2 = _getResp(ui.prompt("是否已经比对过本次代码的新老版本(y/n)\\n",default="n"))
        if resp2:
            ui.write("准备提交本次修改...\\n")
            commands.commit(ui, repo, *pats, **opts)
            ui.write("本次修改已经提交到本地")
        else:
            # 开启代码比对插件
            pass
    else:
        ui.write("放弃本次本地修改...\\n")

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
    resp = _getResp(ui.prompt("确认要提交代码到代码库吗?(y/n)\\n",default="n"))
    if resp:
        ui.warn("准备推送代码到代码库...\\n")
        commands.push(ui, repo, dest, **opts)
        ui.write("代码推送完毕...\\n")
    else:
        ui.write("放弃本次提交...\\n")

def _getResp(resp):
    return resp in ("y","Y","YES","Yes","yes","1")